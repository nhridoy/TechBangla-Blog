from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from techuser.models import UserProfile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email Address",
                             widget=forms.TextInput(attrs={'placeholder': "example@email.com"}))
    last_name = forms.CharField(required=True, label="Last Name",
                                widget=forms.TextInput(attrs={'placeholder': "Last Name"}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': "First Name"}),
            'username': forms.TextInput(attrs={'placeholder': "username"}),
        }

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class UserBasicChange(forms.ModelForm):
    email = forms.EmailField(required=True, label="Email Address",
                             widget=forms.TextInput(attrs={'placeholder': "example@email.com"}))
    last_name = forms.CharField(required=True, label="Last Name",
                                widget=forms.TextInput(attrs={'placeholder': "Last Name"}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class UserBasicChange2(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_pic', 'about', 'website', 'facebook', 'twitter', 'linkedin', 'github',)


class UserBasicChange3(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_pic',)
