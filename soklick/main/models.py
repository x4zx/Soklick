from django.db import models
from django.contrib.auth.models import User

class LinksUsers(models.Model):
    user = models.ForeignKey(
        to = User,
        verbose_name = 'Пользователь',
        on_delete = models.CASCADE
    )
    before_url = models.CharField(
        verbose_name = 'Ссылка:',
        max_length = 250, 
    )
    after_url = models.CharField(
        verbose_name = 'Название для ссылки:',
        max_length = 50,
        unique = True
    )

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'