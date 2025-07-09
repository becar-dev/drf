from rest_framework import serializers
from rsa.prime import is_prime
from django.contrib.auth.models import User
from .models import Subject, Course, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    subject_title = serializers.CharField(source='subject.title', read_only=True)
    subject_id = serializers.PrimaryKeyRelatedField(
        queryset=Subject.objects.all(),
        source='subject',
        write_only=True
    )
    average_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Course
        fields = [
            'id', 'title', 'overview', 'duration', 'price',
            'owner', 'image', 'subject_id', 'subject_title',
            'created', 'average_rating', 'is_premium'
        ]
        read_only_fields = ['owner', 'created']



class CourseInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title']

class SubjectSerializer(serializers.ModelSerializer):
    courses = CourseInlineSerializer(many=True, read_only=True)
    course_count = serializers.SerializerMethodField()

    class Meta:
        model = Subject
        fields = ['id', 'title', 'slug', 'image', 'courses', 'course_count']


    def get_course_count(self, obj):
        return obj.courses.count()


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
        # `password2` maydonini `validated_data`dan olib tashlaymiz,
        # chunki u `User` modelida mavjud emas.
        validated_data.pop('password2')

        user = User.objects.create(
            username=validated_data['username']
        )

        # Parolni shifrlab (set_password) saqlaymiz.
        user.set_password(validated_data['password'])
        user.save()

        return user


# ----------------------------------------------------------------

class LoginSerializer(serializers.Serializer):
    """
    Tizimga kirish uchun `username` va `password`ni qabul qiluvchi serializer.
    Bu serializer modelga bog'lanmagan.
    """
    username = serializers.CharField(required=True)
    password = serializers.CharField(
        required=True,
        write_only=True,  # Parol javobda qaytarilmasligi uchun
        style={'input_type': 'password'}
    )


# ----------------------------------------------------------------

class LogoutJWTSerializer(serializers.Serializer):
    """
    JWT orqali tizimdan chiqish uchun `refresh` tokenini qabul qiluvchi serializer.
    """
    refresh = serializers.CharField(help_text="JWT bilan tizimdan chiqish uchun refresh token")
