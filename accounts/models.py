from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField()
    nickname = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=[('M', '남성'), ('F', '여성')])
    age = models.PositiveIntegerField()
    weekly_reading = models.PositiveIntegerField(default=0)
    yearly_goal = models.PositiveIntegerField()  # 연간 독서량
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    interests = models.CharField(max_length=100, blank=True)
    followings = models.ManyToManyField(
            'self',
            symmetrical=False,
            related_name='followers',
            blank=True
        )
    def __str__(self):
        return self.username