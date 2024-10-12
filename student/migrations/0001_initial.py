# Generated by Django 5.1.2 on 2024-10-11 14:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("api", "0002_alter_sponsor_full_name_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="OTM",
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
                ("nomi", models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Student",
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
                ("f_i_sh", models.CharField(max_length=255, verbose_name="F.I.SH")),
                (
                    "telefon_raqam",
                    models.CharField(
                        max_length=20, unique=True, verbose_name="TELEFON RAQAM"
                    ),
                ),
                (
                    "talabalik_turi",
                    models.CharField(
                        choices=[
                            ("barchasi", "Barchasi"),
                            ("bakalavr", "Bakalavr"),
                            ("magistr", "Magistr"),
                        ],
                        default="barchasi",
                        max_length=20,
                        verbose_name="TALABALIK TURI",
                    ),
                ),
                (
                    "kontrakt_miqdori",
                    models.DecimalField(
                        decimal_places=2, max_digits=12, verbose_name="KONTRAKT MIQDORI"
                    ),
                ),
                (
                    "ajratilgan_summa",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=12,
                        null=True,
                        verbose_name="AJRATILGAN SUMMA",
                    ),
                ),
                (
                    "otm",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="students",
                        to="student.otm",
                    ),
                ),
                (
                    "sponsor",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="students",
                        to="api.sponsor",
                    ),
                ),
            ],
        ),
    ]
