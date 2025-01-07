from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profiles
from django.utils.translation import gettext_lazy as _

class Login_Form(forms.ModelForm):
    username=forms.CharField(label= 'الاسم',max_length=100, required=False)
    password=forms.CharField(label='كلمة المرور', widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('username','password')





class userCreationForms(UserCreationForm):
    username = forms.CharField(label='الاسم', max_length=100)
    first_name = forms.CharField(label='الاسم الأول', max_length=100)
    last_name = forms.CharField(label='الاسم الأخير', max_length=100)
    email = forms.EmailField(label='البريد', max_length=100)
    password1 = forms.CharField(label='كلمة المرور', widget=forms.PasswordInput(), max_length=8)
    password2 = forms.CharField(label='تأكيد كلمة المرور', widget=forms.PasswordInput(), max_length=8)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')





class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(label=_("الاسم الأول"), max_length=50)
    last_name = forms.CharField(label=_("الاسم الأخير"), max_length=50)
    email = forms.EmailField(label=_("البريد الإلكتروني"), max_length=254)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')





class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = ('name', 'surname')
