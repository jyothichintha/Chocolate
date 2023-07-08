from django import forms
from app.models import *

class UserForm(forms.ModelForm):
    class Meta():
        model=User
        model=User
        fields=['username','email','password']
        widgets={'password':forms.PasswordInput()}

class ChocolateForm(forms.ModelForm):
    class Meta():
        model = Chocolate
        fields = '__all__'
    