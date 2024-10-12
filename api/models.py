from django.db import models


class Sponsor(models.Model):
    PERSON_TYPE_CHOICES = (
        ('jismoniy', 'Jismoniy Shaxs'),
        ('yuridik', 'Yuridik Shaxs'),
    )

    PAYMENT_AMOUNT_CHOICES = [
        (1000000, '1 000 000 UZS'),
        (5000000, '5 000 000 UZS'),
        (7000000, '7 000 000 UZS'),
        (10000000, '10 000 000 UZS'),
        (30000000, '30 000 000 UZS'),
        ('other', 'Boshqa'),
    ]

    PAYMENT_CHOICES = (
        ('pul', 'Pul o`tkazmalari'),
    )

    STATUS_CHOICES = (
        ('yangi', 'Yangi'),
        ('tasdiqlangan', 'Tasdiqlangan'),
        ('bekor_qilingan', 'Bekor qilingan'),
        ('moderatsiya', 'Moderatsiyada'),
    )

    person_type = models.CharField('SHAXS', max_length=10, choices=PERSON_TYPE_CHOICES)
    full_name = models.CharField("F.I.SH", max_length=255)
    phone_number = models.CharField("TELEFON RAQAMINGIZ:+998", max_length=13)
    payment_amount = models.CharField("TO'LOV SUMMASI", choices=PAYMENT_AMOUNT_CHOICES, max_length=50)
    other_payment_amount = models.PositiveIntegerField("BOSHQA SUMMA", null=True, blank=True)
    organization_name = models.CharField("TASHKILOT NOMI", max_length=255, blank=True, null=True)
    spent_amount = models.PositiveIntegerField('SARFLANGAN SUMMA', default=0)
    date = models.DateField(auto_now_add=True)
    status = models.CharField('HOLATI', max_length=20, choices=STATUS_CHOICES, default='yangi')
    payment_type = models.CharField('TO`LOV TURI', choices=PAYMENT_CHOICES, max_length=50, blank=True, null=True)  # To'lov turi

    def __str__(self):
        return self.full_name
