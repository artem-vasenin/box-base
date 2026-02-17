from django.db import models


class Excursion(models.Model):
    """ Модель заявки на экскурсию """
    name = models.CharField(max_length=100, verbose_name='Имя')
    kid_name = models.CharField(max_length=100, verbose_name='Имя ребёнка')
    phone = models.CharField(max_length=12, unique=True, verbose_name='Телефон')
    email = models.EmailField(max_length=100, unique=True, verbose_name='E-mail')
    description = models.TextField(null=True, blank=True, verbose_name='Желаемая дата и время, вопросы')
    is_agree = models.BooleanField(default=False, blank=True, verbose_name='Согласие на обработку персональных данных')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        verbose_name = "Заявка на экскурсию"
        verbose_name_plural = "Заявки на экскурсию"

    def __str__(self):
        return f'{self.name}: "{self.phone}" ({self.kid_name})'
