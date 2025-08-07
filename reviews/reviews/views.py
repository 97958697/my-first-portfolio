from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Movie, Review
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ReviewForm, MovieForm


def index(request):
    """レビュー一覧を表示するビュー"""
    reviews = Review.objects.all()
    return render(request, 'mock_index.html', {'reviews': reviews})

def detail(request, review_id):
    """指定されたレビュー詳細を表示するビュー"""
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'mock_detail.html', {'review': review})

@login_required
def create(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.user = request.user
            review.save()
            return redirect('reviews:detail', review_id=review.id)
    else:
        form = ReviewForm()
    return render(request, 'reviews/create.html', {'form': form, 'movie': movie})

@login_required
def delete(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    if request.method == 'POST':
        review.delete()
        return redirect('reviews:index')
    return render(request, 'reviews/delete.html', {'review': review})

@login_required
def update(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('reviews:movie_detail', pk=review.movie.pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'reviews/update.html', {'form': form, 'review': review})

@login_required
def manage(request, movie_id):
 """ログインユーザーの当該映画レビュー管理ページ"""
 movie = get_object_or_404(Movie, pk=movie_id)
 reviews = Review.objects.filter(movie=movie, user=request.user)
 return render(request, 'reviews/manage.html', {'movie': movie, 'reviews': reviews})


# Movie Views
class MovieListView(ListView):
    model = Movie
    template_name = 'reviews/movie_list.html'
    context_object_name = 'movies'

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'reviews/movie_detail.html'
    context_object_name = 'movie'

class MovieCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'reviews/movie_form.html'
    success_url = reverse_lazy('reviews:movie_list')
    def test_func(self):
        return self.request.user.is_staff

class MovieUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'reviews/movie_form.html'
    success_url = reverse_lazy('reviews:movie_list')
    def test_func(self):
        return self.request.user.is_staff

class MovieDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Movie
    template_name = 'reviews/movie_confirm_delete.html'
    success_url = reverse_lazy('reviews:movie_list')
    def test_func(self):
        return self.request.user.is_staff
