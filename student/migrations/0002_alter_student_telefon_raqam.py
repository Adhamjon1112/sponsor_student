# Generated by Django 5.1.2 on 2024-10-11 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="telefon_raqam",
            field=models.CharField(
                max_length=12, unique=True, verbose_name="TELEFON RAQAM : +998"
            ),
        ),
    ]
