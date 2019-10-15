from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(help_text="",label='Email', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your email: '}))
    first_name = forms.CharField(help_text="",max_length=20, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your first name'}))
    last_name = forms.CharField(help_text="",max_length=20, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your last name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder']= 'Enter your username'
        self.fields['username'].label = 'Username'
        self.fields['username'].help_text = ''
        self.fields['password1'].widget.attrs['placeholder']= 'Enter your password'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].label = 'Password'
        self.fields['password1'].help_text = "<ul class='form-text text-muted small'><li>Your password can't be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can't be a commonly used password.</li><li>Your password can't be entirely numeric.</li></ul>"
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].label = 'Password confirmation'
        self.fields['password2'].widget.attrs['placeholder']= 'Enter your password again'
        self.fields['password2'].help_text = ''

class EditProfileForm(UserChangeForm):
    password = forms.CharField(label='', widget=forms.TextInput(attrs={'type':'hidden'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')
        # exclude = () PASAS LOS FIELDS QUE QUERES SACAR
