from django import forms

from task.models import User,Todo


from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):

    class Meta:

        model=User

        fields=["username","email","password1","password2","phone"]




class SignInForm(forms.Form):

    username=forms.CharField(max_length=20)

    password=forms.CharField(max_length=20)

    


class TodoForm(forms.ModelForm):
   
    class Meta:

        model=Todo

        fields=["title"]

        

       




    