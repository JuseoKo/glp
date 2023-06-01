from django.db import models

class Cash(models.Model):
    master = models.CharField(primary_key=True, null=False, max_length=20)
    money = models.CharField(max_length=10, null=False)