from django.db import models

class BaseNews(models.Model):
    news_code = models.CharField(primary_key=True, verbose_name='뉴스코드')
    Publisher = models.CharField(max_length=20, null=False, verbose_name='퍼블리셔')
    created_at = models.DateTimeField(auto_now_add==True, verbose_name='생성시간')
    update_at = models.DateTimeField(auto_now=True, verbose_name='업데이트 시간')
