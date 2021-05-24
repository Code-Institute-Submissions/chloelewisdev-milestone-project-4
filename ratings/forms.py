from django import forms
from .models import Rating


class RatingForm(forms.ModelForm):

    class Meta:
        model = Rating
        exclude = ('user_profile', 'created_on', 'product',)
    
    rating_score = forms.IntegerField(
        label='Rating 1-5',
        widget=forms.NumberInput(
            attrs={'min': 1, 'max': 5, 'class': 'text-center'}
        )
    )
