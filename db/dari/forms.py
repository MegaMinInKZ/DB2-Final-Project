from django.contrib.auth.forms import UserCreationForm
from django.core.files.images import get_image_dimensions
from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator



class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'category', 'price', 'amount', 'Image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'full-width',
                                            'required': True,}),
            'category': forms.Select(attrs={'class': 'full-width',
                                            'required': True}),
            'price': forms.NumberInput(attrs={'class': 'full-width',
                                              'required': True}),
            'amount': forms.NumberInput(attrs={'class': 'full-width',
                                              'required': True}),
            'Image': forms.ClearableFileInput(attrs={'class': 'full-width',
                                               'required': True})
        }
    def __init__(self, *args, **kwargs ):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Category isn't chosen"

    def clean_Image(self):
        image = self.cleaned_data['Image']
        width, height = get_image_dimensions(image.file)
        if width > 1000 or height > 1000 or height < 100 or width < 100:
            raise forms.ValidationError("Image height, width should be less than 1000px and more than 100px")
        if image.size > 0.5 * 1024 * 1024:
            raise forms.ValidationError("Image size should be less than 2MB")
        return image



