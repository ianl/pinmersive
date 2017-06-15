from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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