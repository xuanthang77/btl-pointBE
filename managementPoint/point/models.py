from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)
    avatar = models.ImageField(upload_to="point/static/users/%Y/%m/",null=True, blank=True)
    email_domain = models.CharField(max_length=100, null=True, blank=True)

class Subject(models.Model):
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=100, null=True, blank=True)
    lecturer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

class Grade(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    midterm_grade = models.FloatField()
    final_grade = models.FloatField()
    other_grade_1 = models.FloatField(null=True, blank=True)
    other_grade_2 = models.FloatField(null=True, blank=True)
    other_grade_3 = models.FloatField(null=True, blank=True)
    other_grade_4 = models.FloatField(null=True, blank=True)
    other_grade_5 = models.FloatField(null=True, blank=True)
    is_locked = models.BooleanField(default=False)

class ForumPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class ForumComment(models.Model):
    post = models.ForeignKey(ForumPost, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
