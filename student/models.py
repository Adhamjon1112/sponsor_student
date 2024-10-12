from django.db import models
from api.models import Sponsor

class OTM(models.Model):
    nomi = models.CharField(max_length=255, unique=True)  

    def __str__(self):
        return self.nomi

class Student(models.Model):
    TALABALIK_TURI_CHOICES = [
        ('barchasi', 'Barchasi'),
        ('bakalavr', 'Bakalavr'),
        ('magistr', 'Magistr'),
    ]

    f_i_sh = models.CharField("F.I.SH", max_length=255)  
    telefon_raqam = models.CharField("TELEFON RAQAM : +998", max_length=12, unique=True)  
    otm = models.ForeignKey(OTM, related_name='students', on_delete=models.CASCADE)  
    talabalik_turi = models.CharField("TALABALIK TURI", max_length=20, choices=TALABALIK_TURI_CHOICES, default='barchasi')  # Talabalik turi
    kontrakt_miqdori = models.DecimalField("KONTRAKT MIQDORI", max_digits=12, decimal_places=2)  
    sponsor = models.ForeignKey(Sponsor, related_name='students', on_delete=models.SET_NULL, null=True, blank=True)  
    ajratilgan_summa = models.DecimalField("AJRATILGAN SUMMA", max_digits=12, decimal_places=2, null=True, blank=True)  # Ajratilgan summa

    def __str__(self):
        return self.f_i_sh