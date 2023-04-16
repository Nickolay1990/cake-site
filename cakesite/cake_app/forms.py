from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import *
from captcha.fields import CaptchaField


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-input-product-name'}),
            'price': forms.NumberInput(
                attrs={'class': 'form-input-product-price'})
        }

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise ValidationError('Цена не может быть меньше 0')
        return price


class AddCakeForm(forms.ModelForm):
    class Meta:
        model = Cake
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input-cake-name'}),
            'slug': forms.TextInput(attrs={'class': 'form-input-cake-slug'}),
            'description': forms.Textarea(
                attrs={'class': 'form-input-cake-description'}),
            'photo': forms.FileInput(attrs={'class': 'form-input-cake-photo'}),
        }


class AddTechCardForm(forms.ModelForm):
    class Meta:
        model = TechCard
        fields = '__all__'
        widgets = {'quantity': forms.NumberInput(
            attrs={'class': 'form-input-techcard-quantity'})}

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity <= 0:
            raise ValidationError('Количество не может быть меньше 0')
        return quantity


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput())
    email = forms.EmailField(label='Email', widget=forms.EmailInput())
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повторите пароль',
                                widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput())
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Имя')
    email = forms.EmailField()
    content = forms.CharField(label='Содержание',
                              widget=forms.Textarea(
                                  attrs={'cols': 50, 'rows': 10}))
    captcha = CaptchaField(label='Введите каптчу')
