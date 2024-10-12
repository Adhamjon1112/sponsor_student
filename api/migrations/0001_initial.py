# Generated by Django 5.1.2 on 2024-10-10 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Sponsor",
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
                    "person_type",
                    models.CharField(
                        choices=[
                            ("jismoniy", "Jismoniy Shaxs"),
                            ("yuridik", "Yuridik Shaxs"),
                        ],
                        max_length=10,
                    ),
                ),
                ("full_name", models.CharField(max_length=255, verbose_name="F.I.SH.")),
                (
                    "phone_number",
                    models.CharField(max_length=15, verbose_name="Telefon Raqamingiz"),
                ),
                (
                    "payment_amount",
                    models.CharField(max_length=20, verbose_name="To'lov Summasi"),
                ),
                (
                    "other_payment_amount",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="Boshqa To'lov Summasi"
                    ),
                ),
                (
                    "organization_name",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Tashkilot Nomi",
                    ),
                ),
                ("spent_amount", models.PositiveIntegerField(default=0)),
                ("date", models.DateField(auto_now_add=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("yangi", "Yangi"),
                            ("tasdiqlangan", "Tasdiqlangan"),
                            ("bekor_qilingan", "Bekor qilingan"),
                        ],
                        default="yangi",
                        max_length=20,
                    ),
                ),
                (
                    "payment_type",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
            ],
        ),
    ]