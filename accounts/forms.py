from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class RegistrationForm(UserCreationForm):
    role = forms.ChoiceField(choices=User.Roles.choices)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'phone',
            'role',
            'city',
            'state',
            'address',
            'password1',
            'password2',
        )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'phone', 'city', 'state', 'address')
