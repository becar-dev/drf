from rest_framework import serializers
from .models import Subject, Course

class CourseSerializer(serializers.ModelSerializer):
    subject_title = serializers.CharField(source='subject.title', read_only=True)
    subject_id = serializers.PrimaryKeyRelatedField(
        queryset=Subject.objects.all(),
        source='subject',
        write_only=True
    )

    class Meta:
        model = Course
        fields = [
            'id', 'title', 'overview', 'duration', 'price',
            'owner', 'image', 'subject_id', 'subject_title', 'created'
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
