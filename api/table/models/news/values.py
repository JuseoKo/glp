from .base import BaseNews
from django.db import models

class NewsValues(models):
    created_at = models.DateTimeField(auto_now_add=True, null=False, verbose_name='생성 시간')
    value = models.JSONField(null=False)
    date = models.DateField(null=False, auto_now_add=True, verbose_name='데이터 시간')
