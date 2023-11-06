from models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class NewUserForm(UserCreationForm):
    class Meta:
        mode=User
        fildls = ['username', 'email', 'password', 'password_confirmation']

class AddProductForm(ModelForm):
    class Meta:
        model = Producto
        fildls = '__all__'