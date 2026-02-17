from django import forms

from .models import Excursion


class ExcursionForm(forms.ModelForm):
    """ Форма заявки на экскурсию """
    rating = forms.ChoiceField(
        choices=[(i, '★') for i in range(1, 6)],
        widget=forms.RadioSelect(attrs={'required': True})
    )

    class Meta:
        model = Excursion
        fields = ['name', 'kid_name', 'phone', 'email', 'description', 'is_agree']
        widgets = {
            'description': forms.Textarea(attrs={
                'placeholder': 'Your comment...', 'rows': 4, 'min-length': 20, 'required': True, 'class': 'Textarea'
            }),
        }