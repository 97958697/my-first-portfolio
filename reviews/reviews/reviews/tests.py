from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from .models import Movie, Review
from .forms import MovieForm, ReviewForm
import datetime
from django.db import IntegrityError

User = get_user_model()

class ModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass')
        self.movie = Movie.objects.create(
            title='Test Movie',
            description='Desc',
            release_date=timezone.now().date()
        )

    def test_unique_user_movie_review_constraint(self):
        Review.objects.create(user=self.user, movie=self.movie, rating=3, comment='')
        with self.assertRaises(IntegrityError):
            Review.objects.create(user=self.user, movie=self.movie, rating=4, comment='dup')

    def test_rating_validator(self):
        review = Review(user=self.user, movie=self.movie, rating=6, comment='')
        with self.assertRaises(Exception):
            review.full_clean()

class FormTests(TestCase):
    def test_movie_form_future_date_invalid(self):
        data = {
            'title': 'F',
            'description': 'D',
            'release_date': (timezone.now().date() + datetime.timedelta(days=1))
        }
        form = MovieForm(data)
        self.assertFalse(form.is_valid())
        self.assertIn('release_date', form.errors)

    def test_review_form_rating_range(self):
        data = {'rating': 0, 'comment': ''}
        form = ReviewForm(data)
        self.assertFalse(form.is_valid())
        self.assertIn('rating', form.errors)

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='viewer', password='pass')
        self.movie = Movie.objects.create(
            title='View Movie',
            description='Desc',
            release_date=timezone.now().date()
        )

    def test_movie_list_view(self):
        url = reverse('reviews:movie_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/movie_list.html')

    def test_movie_detail_view(self):
        url = reverse('reviews:movie_detail', args=[self.movie.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.movie.title)

    def test_review_create_requires_login(self):
        url = reverse('reviews:create', args=[self.movie.pk])
        response = self.client.get(url)
        self.assertRedirects(response, '/accounts/login/?next=' + url)

    def test_review_create_post(self):
        self.client.login(username='viewer', password='pass')
        url = reverse('reviews:create', args=[self.movie.pk])
        response = self.client.post(url, {'rating': 5, 'comment': 'Good'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Review.objects.filter(user=self.user, movie=self.movie).exists())