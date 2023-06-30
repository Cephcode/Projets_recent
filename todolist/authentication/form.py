from django import forms
from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class Sign_up(UserCreationForm):



        class Meta(UserCreationForm.Meta):
                model=get_user_model()
                # fields=["username","password"]
                help_texts = {
                        'username': None,
                        'password': None,
                        # 'password': None,
        }
                widgets={
                        "username":forms.TextInput(attrs={"id":"form3Example1cg","class":"field",'placeholder':'enter your name'}),
                        "password":forms.PasswordInput(attrs={"id":"form3Example2cg","class":"field",'placeholder':'your password'}),
                        # "password2":forms.PasswordInput(attrs={"id":"form3Example2cg","class":"field",'placeholder':'confirm your password'}),
                        }
                # def __init__(self, *args, **kwargs):
                #         super(Sign_up, self).__init__(*args, **kwargs)

                #         for fieldname in ['username', 'password']:
                #                 self.fields[fieldname].help_text = None
                
 
class LoginForm(forms.Form):
        username = forms.CharField(max_length=63, label='Nom d’utilisateur',widget=forms.TextInput(attrs={'placeholder': 'username'}))
        password = forms.CharField(max_length=63, widget=forms.PasswordInput(attrs={'placeholder': 'password'}),label='Mot de passe')