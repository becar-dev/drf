from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Subject, Course, Module, Comment

# ===============================================================
# 1. ASOSIY MODELLAR UCHUN SERIALIZERLAR (OPTIMIZED)
# ===============================================================

class CommentSerializer(serializers.ModelSerializer):
    """
    Izohlar uchun serializer. Foydalanuvchi nomini ham qo'shib ko'rsatadi.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ['id', 'owner', 'course', 'rating', 'created_at']


class ModuleSerializer(serializers.ModelSerializer):
    """
    Modullar uchun serializer.
    """
    class Meta:
        model = Module
        fields = ['id', 'title', 'course']


class CourseListSerializer(serializers.ModelSerializer):
    """
    KATTA OPTIMIZATSIYA: Kurslar ro'yxati (/api/courses/) uchun yengil serializer.
    Bu faqat asosiy va annotatsiya qilingan ma'lumotlarni ko'rsatadi.
    """
    # View'da annotate() orqali qo'shilgan maydonlar
    average_rating = serializers.FloatField(read_only=True, default=0)
    modules_count = serializers.IntegerField(read_only=True, default=0)
    comments_count = serializers.IntegerField(read_only=True, default=0)
    subject_title = serializers.CharField(source='subject.title', read_only=True)

    class Meta:
        model = Course
        fields = [
            'id', 'title', 'image', 'is_premium', 'price',
            'subject_title', 'average_rating', 'modules_count', 'comments_count'
        ]


class CourseDetailSerializer(serializers.ModelSerializer):
    """
    KATTA OPTIMIZATSIYA: Bitta kurs haqida to'liq ma'lumot (/api/courses/1/) uchun serializer.
    View'da prefetch_related() ishlatilgani uchun bu maydonlar qo'shimcha so'rov yubormaydi.
    """
    # Nested serializers for related models
    modules = ModuleSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    # Annotate qilingan maydonlar
    average_rating = serializers.FloatField(read_only=True, default=0)

    # Yozish uchun alohida, o'qish uchun alohida maydonlar
    # XATOLIK TUZATILDI: serializersPrimaryKeyRelatedField -> serializers.PrimaryKeyRelatedField
    subject = serializers.PrimaryKeyRelatedField(
        queryset=Subject.objects.all(), write_only=True
    )
    subject_title = serializers.CharField(source='subject.title', read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Course
        fields = [
            'id', 'title', 'overview', 'duration', 'price', 'is_premium',
            'owner', 'image', 'created', 'subject', 'subject_title',
            'average_rating', 'modules', 'comments'
        ]


class SubjectSerializer(serializers.ModelSerializer):
    """
    Fanlar uchun serializer.
    """
    # OPTIMIZATSIYA: `SerializerMethodField` o'rniga `IntegerField` ishlatildi.
    # Bu `views.py` dagi `annotate(course_count=Count('courses'))` bilan birga ishlaydi.
    course_count = serializers.IntegerField(read_only=True)

    # `prefetch_related('courses')` bilan samarali ishlaydi.
    # Kurslar ro'yxati uchun yengil serializer ishlatamiz.
    courses = CourseListSerializer(many=True, read_only=True)

    class Meta:
        model = Subject
        fields = ['id', 'title', 'slug', 'image', 'course_count', 'courses']


# ===============================================================
# 2. AUTENTIFIKATSIYA UCHUN SERIALIZERLAR (O'zgarishsiz)
# ===============================================================

class RegisterSerializer(serializers.ModelSerializer):
    """
    Foydalanuvchini ro'yxatdan o'tkazish uchun serializer.
    Parolni tasdiqlash uchun `password2` maydoni qo'shilgan.
    """
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'},
        help_text="Foydalanuvchi paroli"
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        label='Parolni tasdiqlang',
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ('username', 'password', 'password2')
        extra_kwargs = {
            'username': {'help_text': 'Noyob foydalanuvchi nomi (username)'},
        }

    def validate(self, attrs):
        """
        Ikkala parolning bir-biriga mosligini tekshiradi.
        """
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Parollar bir-biriga mos kelmadi."})
        return attrs

    def create(self, validated_data):
        """
        Validatsiyadan o'tgan ma'lumotlar asosida yangi foydalanuvchi yaratadi.
        Parol xeshlanadi (hashed).
        """
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    """
    Tizimga kirish uchun `username` va `password`ni qabul qiluvchi serializer.
    Bu serializer modelga bog'lanmagan.
    """
    username = serializers.CharField(required=True)
    password = serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type': 'password'}
    )


class LogoutJWTSerializer(serializers.Serializer):
    """
    JWT orqali tizimdan chiqish uchun `refresh` tokenini qabul qiluvchi serializer.
    """
    refresh = serializers.CharField(help_text="JWT bilan tizimdan chiqish uchun refresh token")
