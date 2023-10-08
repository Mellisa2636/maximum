from django import forms
from .models import Advertisements
from django.core.exceptions import ValidationError

# Create your forms here.

class AdvertisementForms(forms.ModelForm):
    class Meta:
        model = Advertisements
        fields = ("title", "description", "image", "price", "auction")
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control form-control-lg'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control form-control-lg'}),
            'image': forms.FileInput(attrs={
                'class': 'form-control form-control-lg'}),
            'price': forms.NumberInput(attrs={
                'class': 'form-control form-control-lg'}),
            'auction': forms.CheckboxInput(attrs={
                'class': 'form-check-input'})
        }

    
    def clean_title(self):
            title = self.cleaned_data['title']
            if title.startswith('?'):
                raise ValidationError('Заголовок не может начинаться с вопросительного знака.')
            return title