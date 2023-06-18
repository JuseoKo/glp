# Generated by Django 4.2.1 on 2023-06-15 14:41

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BaseNews",
            fields=[
                (
                    "news_code",
                    models.CharField(
                        primary_key=True, serialize=False, verbose_name="뉴스코드"
                    ),
                ),
                ("Publisher", models.CharField(max_length=20, verbose_name="퍼블리셔")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="생성시간"),
                ),
                (
                    "update_at",
                    models.DateTimeField(auto_now=True, verbose_name="업데이트 시간"),
                ),
            ],
            options={
                "db_table": "base_news",
            },
        ),
        migrations.CreateModel(
            name="NewsValues",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="생성 시간"),
                ),
                ("value", models.JSONField()),
                ("date", models.DateField(auto_now_add=True, verbose_name="데이터 시간")),
            ],
            options={
                "db_table": "news_values",
            },
        ),
        migrations.CreateModel(
            name="Test",
            fields=[
                (
                    "name",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("money", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "test",
            },
        ),
    ]