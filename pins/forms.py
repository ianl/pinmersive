from django import forms

from .models import Pin
from boards.models import Board

class NewPinForm(forms.ModelForm):
    class Meta:
        model = Pin
        fields = ['image_file', 'image_url', 'board', 'description']

class NewPinFromWebForm(forms.ModelForm):
    image_url = forms.URLField(required=True)
    board = forms.ModelChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(NewPinFromWebForm, self).__init__(*args, **kwargs)
        
        self.fields['board'].queryset = Board.objects.filter(user_profile__user=user)

    class Meta:
        model = Pin
        fields = ['image_url', 'board', 'description']

class NewPinFromDeviceForm(forms.ModelForm):
    image_file = forms.ImageField(required=True)
    board = forms.ModelChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(NewPinFromDeviceForm, self).__init__(*args, **kwargs)
        
        self.fields['board'].queryset = Board.objects.filter(user_profile__user=user)
    
    class Meta:
        model = Pin
        fields = ['image_file', 'board', 'description']

class EditPinForm(forms.ModelForm):
    board = forms.ModelChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(EditPinForm, self).__init__(*args, **kwargs)
        
        self.fields['board'].queryset = Board.objects.filter(user_profile__user=user)

    class Meta:
        model = Pin
        fields = ['board', 'description']