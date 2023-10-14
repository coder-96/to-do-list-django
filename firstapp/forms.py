from django.forms import ModelForm
from .models import User, Todo

from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "password1", "password2"]


class TodosForm(ModelForm):
    class Meta:
        model = Todo
        fields = ["name", "done"]


class UserForm(ModelForm):
    class Meta:
        model = User
        # fields = "__all__"
        fields = ["avatar", "name", "email", "bio"]


class PasswordUpdateForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = "__all__"
