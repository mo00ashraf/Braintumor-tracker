from django import forms
from .models import Image , Files
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('image',)


from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['firstname','lastname', 'email', 'profile_picture']
        labels = {
            'firstname': 'First Name',
            'lastname': 'Last Name',
            'email': 'Email Address',
            'profile_picture': 'Profile Picture',
        }
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'custom-input'}),
            'lastname': forms.TextInput(attrs={'class': 'custom-input'}),
            'email': forms.EmailInput(attrs={'class': 'custom-input'}),
            'profile_picture': forms.FileInput(attrs={'class': 'custom-input'}),
        }
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        user = instance.user
        user.first_name = instance.firstname
        user.last_name = instance.lastname
        user.save()
        if commit:
            instance.save()
        return instance

