from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, CharField, PasswordInput


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control col-lg-2',
            }),
            'email': EmailInput(attrs={
                'class': 'form-control col-lg-2',
            }),
        }

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'form-control col-lg-2'
        self.fields['password2'].widget.attrs['class'] = 'form-control col-lg-2'


class Authenticate(AuthenticationForm):
    fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(Authenticate, self).__init__(*args, **kwargs)

    username = UsernameField(widget=TextInput(
        attrs={'class': 'form-control col-lg-2',
               }))
    password = CharField(widget=PasswordInput(
        attrs={
            'class': 'form-control col-lg-2',
        }))
