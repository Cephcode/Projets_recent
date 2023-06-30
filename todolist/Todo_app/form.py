from django import forms
from .models import Todo
class Todo_form(forms.ModelForm):
    class Meta:
        model=Todo
        fields=["title","description"]
        widgets={
             "title":forms.TextInput(attrs={'placeholder':'enter a title...'}),
            "description":forms.TextInput(attrs={'placeholder':'describe your task'}),
                        
                        }
