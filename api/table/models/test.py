from django.db import models

class Test(models.Model):
    name = models.CharField(primary_key=True, null=False, max_length=20)
    money = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'test'