from django.db import models

class Book(models.Model):
    Name = models.CharField(primary_key=True, null=False, max_length=20)
    colour = models.CharField(max_length=10, null=False)