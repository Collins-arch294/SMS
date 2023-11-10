from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):    
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField() 
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=50,widget=forms.PasswordInput)

# class Report(forms.Form):
# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('picture', 'bio', 'first_name', 'last_name' )

#     def __init__(self, *args, **kwargs):
#         super(ProfileForm, self).__init__(*args, **kwargs)
#         self.fields['picture'].widget.attrs.update({'class': 'form-control-file'})
#         self.fields['bio'].widget.attrs.update({'class': 'form-control', 'rows': 4})
# user update form
# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields =( 'picture', 'bio')
#profile update form
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField() 
    
    class Meta:
        model = Profile
        fields =('first_name', 'last_name','email','picture', 'bio','course', 'school', 'address' )

