import re
from rest_framework import serializers
from .models import Sponsor
from django.contrib.auth.models import User

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['password'] = user.password
        return token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, data):
        user = User.objects.create_user(username=data['username'], password=data['password'])
        return user
    

class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = '__all__'
        read_only_fields = ['spent_amount', 'date', 'status', 'payment_type']

    def validate_phone_number(self, value):
        # Foydalanuvchi faqat 9 ta raqam kiritishi
        if not re.fullmatch(r'\d{9}', value):
            raise serializers.ValidationError("Telefon raqami faqat 9 ta raqamdan iborat bo‘lishi kerak.")
        
        # Birinchi raqam 9 bo‘lishi 
        if not value.startswith('9'):
            raise serializers.ValidationError("Telefon raqamining birinchi raqami 9 bo‘lishi kerak.")
        
        # Avtomatik tarzda +998 qo‘shish
        formatted_number = '+998' + value
        
        return formatted_number

    def validate_payment_amount(self, value):
        if value == 'other' and not self.initial_data.get('other_payment_amount'):
            raise serializers.ValidationError("Boshqa to'lov summasini kiriting.")
        return value

    def validate(self, data):
        person_type = data.get('person_type')
        organization_name = data.get('organization_name')

        if person_type == 'yuridik' and not organization_name:
            raise serializers.ValidationError({
                'organization_name': "Yuridik shaxslar uchun tashkilot nomi majburiy."
            })
        elif person_type == 'jismoniy' and organization_name:
            # Agar jismoniy shaxs bo'lsa va tashkilot nomi berilgan bo'lsa, uni tozalash
            data['organization_name'] = None

        return data

class SponsorDetailSerializer(serializers.ModelSerializer):
    sponsorship_amount = serializers.SerializerMethodField()

    class Meta:
        model = Sponsor
        fields = ['full_name', 'phone_number', 'sponsorship_amount', 'organization_name']

    def get_sponsorship_amount(self, obj):
        if obj.payment_amount is not None and not 'other':
            return obj.payment_amount
        elif obj.other_payment_amount is not None:
            return obj.other_payment_amount
        return None

class SponsorEditSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sponsor
        fields = ['person_type', 'full_name', 'phone_number', 'status', 'payment_amount', 'other_payment_amount', 'payment_type', 'organization_name']


    def validate_phone_number(self, value):
        # Foydalanuvchi faqat 9 ta raqam kiritishi
        if not re.fullmatch(r'\d{9}', value):
            raise serializers.ValidationError("Telefon nomer faqat 9 ta raqamdan iborat bo‘lishi kerak.")
        
        # Birinchi raqam 9 bo‘lishi
        if not value.startswith('9'):
            raise serializers.ValidationError("Telefon nomerning birinchi raqami 9 bo‘lishi kerak.")
        
        # Avtomatik tarzda +998 qo‘shish
        formatted_number = '+998' + value
        
        return formatted_number

