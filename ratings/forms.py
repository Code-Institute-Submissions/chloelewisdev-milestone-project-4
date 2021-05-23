from django import forms
from .models import Rating


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('rating_title', 'rating_description', 'rating_score', )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'rating_title': 'Title',
            'rating_description': 'Description',
            'rating_score': 'Rating',
        }

        self.fields['rating_title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'rating_score':
                if self.fields[field].required:
                    placeholder = placeholders[field]
                    self.fields[field].widget.attrs['placeholder'] = placeholder            
                    self.fields[field].label = False
            
            self.fields[field].widget.attrs['class'] = (
                'border-black rounded-0 profile-form-input')
