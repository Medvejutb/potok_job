from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = models.CharField(max_length=20, null=True, blank=False)
    last_name = models.CharField(max_length=20, blank=True)
    tg = models.CharField(max_length=50)
    rank_choices = [
        ('A', 'Смешарик'),
        ('B', 'Малышарик'),
        ('C', 'Биомасса')
    ]
    rank = models.CharField(
        max_length=10,
        choices=rank_choices,
        default='C'
    )
    points = models.IntegerField(default=0)
    hookah_smoked = models.IntegerField(default=0)
    money_spent = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    def __str__(self):
        return (f'Пользователь {self.first_name} {self.last_name or "Фамилия"} - {self.tg}\n'
                f'Ранг - {self.rank}, очки - {self.points}'
                f'Скурено кальянов - {self.hookah_smoked}'
                f'Потрачено бабла - {self.money_spent}')