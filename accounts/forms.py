from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    '''UserCreationFormのサブクラス'''
    class Meta:
        '''UserCreationFormのインナークラス'''
        model=CustomUser
        fields=('username', 'email', 'password1', 'password2')