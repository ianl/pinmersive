from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils.text import capfirst

from .models import UserProfile

# Users
class NewUserForm(UserCreationForm):
    email = forms.EmailField(max_length=75)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    def clean_username(self):
        data = self.cleaned_data['username']
        data = data.lower()
        return data

    def clean_email(self):
        data = self.cleaned_data['email']
        data = data.lower()

        if User.objects.filter(email=data).count() > 0:
            raise forms.ValidationError("A user with that email already exists.")

        return data

    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        data = data.lower().capitalize()
        return data

    def clean_last_name(self):
        data = self.cleaned_data['last_name']
        data = data.lower().capitalize()
        return data

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class EditUserForm(forms.ModelForm):
    def clean_email(self):
        data = self.cleaned_data['email']
        data = data.lower()

        if User.objects.filter(email=data).exclude(pk=self.instance.pk).count() > 0:
            raise forms.ValidationError("A user with that email already exists.")

        return data

    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        data = data.lower().capitalize()
        return data

    def clean_last_name(self):
        data = self.cleaned_data['last_name']
        data = data.lower().capitalize()
        return data

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

# UserProfiles
class EditUserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['description', 'location', 'avatar']

# Auths
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password = forms.CharField(
        label="", 
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super(AuthenticationForm, self).__init__(*args, **kwargs)

        # Set the label for the "username" field.
        UserModel = get_user_model()
        self.username_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)
        if self.fields['username'].label is None:
            self.fields['username'].label = capfirst(self.username_field.verbose_name)

        self.error_messages['invalid_login'] = (
            "Please enter a correct %(username)s and password. "
            "Note that the password field is case-sensitive."
        )

    def clean_username(self):
        data = self.cleaned_data['username']
        data = data.lower()
        return data
