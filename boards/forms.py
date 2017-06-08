from django import forms
from .models import Board

class NewBoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['name', 'secret']

class EditBoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['name', 'description', 'category', 'secret']