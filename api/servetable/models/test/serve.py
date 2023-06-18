from django.db import models

class ServeTest(models.Model):
    name = models.CharField(max_length=20)
    number = models.IntegerField()

    class Meta:
        db_table = "serve_test"