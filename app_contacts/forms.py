from django import forms
from django.core.validators import RegexValidator

from .models import Excursion


class ExcursionForm(forms.ModelForm):
    """ Форма заявки на экскурсию """
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'Input', 'placeholder': 'Имя', 'id': 'name'})
    )
    kid_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'Input', 'placeholder': 'Имя ребенка', 'id': 'name'})
    )
    phone = forms.CharField(
        max_length=11,
        required=True,
        label='Phone',
        widget=forms.TextInput(
            attrs={'class': 'Input', 'placeholder': '79520000000', 'id': 'phone'}
        ),
        validators=[
            RegexValidator(
                regex=r'^79\d{9}$',
                message='Номер телефона должен начинаться с 79 и содержать 11 цифр, например: 79529999999',
            ),
        ]
    )
    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.EmailInput(
            attrs={'class': 'Input', 'placeholder': 'my@gmail.com', 'id': 'email'}
        )
    )
    description = forms.CharField(
        max_length=9999,
        required=False,
        widget=forms.Textarea(attrs={'class': 'Textarea', 'placeholder': 'Желаемая дата и время, вопросы', 'id': 'description'})
    )

    class Meta:
        model = Excursion
        fields = ['name', 'kid_name', 'phone', 'email', 'description', 'is_agree']
        widgets = {
            'description': forms.Textarea(attrs={
                'placeholder': 'Your comment...', 'rows': 4, 'min-length': 20, 'required': True, 'class': 'Textarea'
            }),
        }