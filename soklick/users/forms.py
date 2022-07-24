from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Registration(UserCreationForm):
    username = forms.CharField(
        label = 'Имя пользователя:',
        max_length = 25,
        min_length = 5,
        required = True,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Admin'
            }
        ),
        help_text = 'Не менее 5 символов! Не более 25 символов! Запрещены: @ , / . + - _ '
    )
    email = forms.EmailField(
        label = 'Email:',
        required = True,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'admin@gmail.com'
            }
        )
    )
    password1 = forms.CharField(
        label = 'Пароль:',
        required = True,
        widget = forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']
    
    def __init__(self, *args, **kwargs):
        super(Registration, self).__init__(*args, **kwargs)
        del self.fields['password2']

class AccountUpdate(forms.ModelForm):
    username = forms.CharField(
        label = 'Имя пользователя:',
        max_length = 25,
        min_length = 5,
        required = True,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Admin'
            }
        ),
        help_text = 'Не менее 5 символов! Не более 25 символов! Запрещены: @ , / . + - _ '
    )
    email = forms.EmailField(
        label = 'Email:',
        required = True,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'admin@gmail.com'
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'email']