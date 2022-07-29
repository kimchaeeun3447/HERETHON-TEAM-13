from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # 기본적으로 제공하는 필드 : username, password
    name = models.CharField(blank=False, max_length=50)
    id_front = models.CharField(null=True, max_length=10)
    id_back = models.CharField(null=True, max_length=10)
    birth_date = models.DateField(null=True)
    level = models.CharField(max_length=10)
    point = models.IntegerField(null=True)
    introduction = models.CharField(max_length=1000)

class Class(models.Model):
    image = models.ImageField(upload_to='classImages', blank=False)
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=10, null=True)
    place = models.TextField()
    isFree = models.CharField(max_length=10, blank=True) #'유료'/'무료'
    class_start_time = models.DateTimeField()
    class_end_time = models.DateTimeField()
    content = models.TextField() 

    class Meta:
        ordering = ['class_start_time'] #클래스 시작일이 촉박한 순으로 정렬
    
    def __str__(self):
        return self.title


class Apply(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE, blank=True)
    applyClass = models.ForeignKey(Class, on_delete = models.CASCADE, blank=True)  
    time = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-time'] #최신순 정렬

    def __str__(self):
        return f"지원자:{self.user} - 클래스:{self.applyClass}"


class Qna(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE, blank=True)
    qnaClass = models.ForeignKey(Class, on_delete = models.CASCADE, blank=True)  
    content = models.TextField()
    time = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-time'] #최신순 정렬

    def __str__(self):
        return f"질문자:{self.user} - 클래스:{self.qnaClass}"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank=True)
    applyClass = models.ForeignKey(Class, on_delete = models.CASCADE, blank=True)
    score = models.IntegerField()
    content = models.TextField()
    time = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-time'] #최신순 정렬

    def __str__(self):
        return f"작성자:{self.user} - 클래스:{self.applyClass}"