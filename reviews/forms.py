from django import forms
from .models import Review, Movie
from django.utils import timezone

class ReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(1, 6)],
        label='Rating'
    )
    class Meta:
        model = Review
        fields = ['rating', 'comment']
class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'image', 'release_date']

    def clean_release_date(self):
        release_date = self.cleaned_data.get('release_date')
        if release_date > timezone.now().date():
            raise forms.ValidationError('公開日は今日以前の日付を指定してください。')
        return release_date