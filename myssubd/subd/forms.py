from .models import User
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, EmailInput, NumberInput, Select, FileInput
from django import forms

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'TelefonPolzovatelya', 'Fotografiya']
        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "first_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отчество'
            }),
            "last_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),

            "TelefonPolzovatelya": TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+X(XXX)XXX-XX-XX'
            }),

            "Fotografiya": FileInput(attrs={'class': 'form-control'}),

        }