from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    """
     * EmailField does automatic email "stuff" like if there isn't an @ symbol django will throw an error saying
        there is something wrong with what you entered.
     * Label is "" because we are going to use placeholder fields so we don't need text above it.
     * widget=forms.TextInput() means the form field that shows up on the screen is a text input or just
        a text box. We pass attrs or attributes to it which allows us to pass different attributes onto
        the page to style our form. Here we use bootstrap which requires a class of form control so we
        can designate that with attrs.
     * placeholder just puts the text passed to it into the text field which goes away when users start
        typing.
     * In first_name and last_name we give it a max_length so users are limited in the length of their name.
    """
    email = forms.EmailField(Label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(Label="", max_length="100",  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(Label="", max_length="100", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Last Name'}))

    """
    The model is User which we imported at the top.
    fields holds everything that the form needs.
    We use password1 and password2 so that we can compare them to make sure that the user does not make
        a mistake when entering their password. Django expects pw1 and pw2 so we have to have them both.
    """
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    """
    Here we are basically doing the same thing that we did for the signupform but for username, password1,
        and password2.
    For these something new is help_text which just gives the user alerts so that they see them if they make
        a mistake when entering these fields.
    We are passing this the SignUpForm.
    """
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
