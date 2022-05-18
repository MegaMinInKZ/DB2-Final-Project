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

def validate_image(image):
    # filesize = image.file.size
    width, height = get_image_dimensions(image.file)
    # if filesize > 2 * 1024 * 1024:
    #     raise forms.ValidationError(_("Image size cannot be more than 2 MB"), params={'value': image})
    if width > 1000 or height > 1000 or height < 100 or width < 100:
        raise forms.ValidationError("Image's height, width should be less than 1000px and more than 100px", params={'value': image})
    return image

class AddProductForm(forms.Form):
    title = forms.CharField(max_length=255)
    price = forms.IntegerField(validators=[MinValueValidator(0)])
    amount = forms.IntegerField(validators=[MinValueValidator(0)])
    Image = forms.ImageField(validators=[validate_image])
    category = forms.ModelChoiceField(queryset=Category.objects.all())



