from django.db import models
from users.models import User
from tabac.models import Tabac
from django.utils import timezone #импортируем файл функций расчета скидок и акции
from django.core.exceptions import ValidationError

def max_valid_check(value): # это функция для проверки максимального значения поля "table"
    if value > 7:
        raise ValidationError('Значение не может быть больше 7')
class Reserv(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=False,
        related_name='reservations'
    )
    start_time = models.DateTimeField()
    table = models.IntegerField(validators=[max_valid_check])

    """
    Хотел внедрить систему расчета скидок с учетом
    временных промежутков, количества и разности вкусов для разных кальянов
    """
    # hookahs = models.IntegerField(max_length=3)
    # mix1 = models.ManyToManyField(
    #     Tabac,
    #     related_name='orders'
    # )
    # mix2 = models.ManyToManyField(
    #     Tabac,
    #     related_name='orders',
    #     blank=True
    # )
    # mix3 = models.ManyToManyField(
    #     Tabac,
    #     related_name='orders',
    #     blank=True
    # )
    # order_time = models.DateTimeField(default=timezone.now())
    #
    # def __str__(self):
    #     mix_list = []
    #     for mix in [self.mix1, self.mix2, self.mix3]:
    #         if mix:
    #             mix_list.append(mix)
    #     return (f'заказ от {self.user} на {self.order_time} - кол-во {self.hookahs}\n'
    #             #f'{["\n".join(mix.__str__())] for m in mix_li}'
    #             f'{mix_list}')