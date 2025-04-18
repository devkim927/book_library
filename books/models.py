from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()

class Book(models.Model):
    title = models.CharField("Title", max_length=200)
    description = models.TextField("Description")
    customer_review_rank = models.FloatField("Customer review rank", null=True, blank=True)
    author = models.CharField("Author", max_length=100)
    cover_image = models.ImageField("Cover image", upload_to='books/', blank=True, null=True)

    # AI 생성 정보
    author_profile_image = models.ImageField("작가 프로필 이미지", upload_to='authors/', blank=True, null=True)
    author_info = models.TextField("작가 정보 (AI 생성)", blank=True)
    author_works = models.TextField("작가 대표작 목록 (AI 생성)", blank=True)

    # gTTS 음성 파일
    audio_file = models.FileField("Voice File", upload_to='tts/', blank=True, null=True)

    def __str__(self):
        return self.title


class Thread(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='threads', default=1)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)  # 선택값 허용
    read_date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover_image = models.ImageField(upload_to='thread_covers/', blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='liked_threads', blank=True)

    def __str__(self):
        return self.title