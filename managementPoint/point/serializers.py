from rest_framework import serializers
from .models import User,Subject, Grade, ForumPost, ForumComment

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        data = validated_data.copy()
        u = User(**data)
        u.set_password(u.password)
        u.save()
        return u
    class Meta:
        model = User
        fields = ['id', 'username','password', 'email', 'role', 'avatar', 'email_domain']
        extra_kwargs = {
            'password': {'write_only': True}
        }
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id','name','class_name','lecturer']

class GradeSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    class Meta:
        model = Grade
        fields = ['id', 'midterm_grade', 'final_grade', 'other_grade_1', 'other_grade_2','other_grade_3','other_grade_4','other_grade_5', 'is_locked','subject','student']


class ForumPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumPost
        fields = '__all__'

class ForumCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumComment
        fields = '__all__'
