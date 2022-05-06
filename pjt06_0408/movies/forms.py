from tkinter import Widget
from django import forms
from .models import Movie

genre_choices =[
    ('코미디','코미디'),
    ('공포','공포'),
    ('로맨스','로맨스')
]

# ModelForm
class MoviesForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Title'
            }
        )
    )
    audience = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Audience'
            }
        )
    )
    genre = forms.ChoiceField(
        choices=genre_choices,
        widget=forms.Select(
            attrs={
                'class':'form-control',
            } 
        ),
    )
    score = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'type':'number',
                'min':0,
                'max':5,
                'step':0.5,
                'placeholder':'Score'
            }
        )
    )
    release_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class':'form-control',
                'type':'date'
            }
        )
    )
    poster_url = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Poster url'
            }
        )
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Description'
            }
        )
    )
    class Meta:
        model = Movie
        fields = '__all__'