# student/serializers.py

import re
from rest_framework import serializers
from .models import OTM, Student
from api.serializers import SponsorSerializer
from api.models import Sponsor

class OTMSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTM
        fields = ['id', 'nomi']

class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'f_i_sh', 'telefon_raqam', 'otm', 'talabalik_turi', 'kontrakt_miqdori']

    def validate_telefon_raqam(self, value):
        if not re.fullmatch(r'\d{9}', value):
            raise serializers.ValidationError("Telefon nomer faqat 9 ta raqamdan iborat bo‘lishi kerak.")
        
        # Birinchi raqam 9 bo‘lishi
        if not value.startswith('9'):
            raise serializers.ValidationError("Telefon nomerning birinchi raqami 9 bo‘lishi kerak.")
        
        # Avtomatik tarzda +998 qo‘shish
        formatted_number = '+998' + value
        
        return formatted_number

    def validate(self, data):
        if data.get('ajratilgan_summa') and data['ajratilgan_summa'] > data['kontrakt_miqdori']:
            raise serializers.ValidationError("Ajratilgan summa kontrakt miqdoridan katta bo'lishi mumkin emas.")
        return data

    def create(self, validated_data):
        student = Student.objects.create(**validated_data)
        return student

class StudentListSerializer(serializers.ModelSerializer):
    otm = OTMSerializer(read_only=True)
    sponsor = SponsorSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'f_i_sh', 'talabalik_turi', 'otm', 'ajratilgan_summa', 'kontrakt_miqdori', 'sponsor']

class StudentDetailSerializer(serializers.ModelSerializer):
    otm = OTMSerializer(read_only=True)
    sponsor = SponsorSerializer(read_only=True)

    class Meta:
        model = Student
        fields = [
            'id',
            'f_i_sh',
            'telefon_raqam',
            'otm',
            'talabalik_turi',
            'sponsor',
            'ajratilgan_summa',
            'kontrakt_miqdori'
        ]

class StudentUpdateSerializer(serializers.ModelSerializer):
    otm = serializers.PrimaryKeyRelatedField(queryset=OTM.objects.all(), required=False)
    
    class Meta:
        model = Student
        fields = [
            'f_i_sh',
            'telefon_raqam',
            'otm',
            'talabalik_turi',
            'kontrakt_miqdori'
        ]

    def validate_telefon_raqam(self, value):
        if not re.fullmatch(r'\d{9}', value):
            raise serializers.ValidationError("Telefon nomer faqat 9 ta raqamdan iborat bo‘lishi kerak.")
        
        # Birinchi raqam 9 bo‘lishi
        if not value.startswith('9'):
            raise serializers.ValidationError("Telefon nomerning birinchi raqami 9 bo‘lishi kerak.")
        
        formatted_number = '+998' + value
        
        return formatted_number

    def validate(self, data):
        if data.get('ajratilgan_summa') and data['ajratilgan_summa'] > data.get('kontrakt_miqdori', self.instance.kontrakt_miqdori):
            raise serializers.ValidationError("Ajratilgan summa kontrakt miqdoridan katta bo'lishi mumkin emas.")
        return data

    def update(self, instance, validated_data):
        otm_data = validated_data.pop('otm', None)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if otm_data is not None:
            instance.otm = otm_data

        instance.save()
        return instance

class StudentAssignSponsorSerializer(serializers.ModelSerializer):
    sponsor = serializers.PrimaryKeyRelatedField(queryset=Sponsor.objects.all())
    ajratilgan_summa = serializers.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        model = Student
        fields = ['sponsor', 'ajratilgan_summa']

    def validate_ajratilgan_summa(self, value):
        if value < 0:
            raise serializers.ValidationError("Ajratilgan summa manfiy bo'lishi mumkin emas.")
        return value

    def update(self, instance, validated_data):
        instance.sponsor = validated_data.get('sponsor', instance.sponsor)
        instance.ajratilgan_summa = validated_data.get('ajratilgan_summa', instance.ajratilgan_summa)
        instance.save()
        return instance
