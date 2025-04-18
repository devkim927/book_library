from django.db import models

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
    title = models.CharField("Title", max_length=200)
    description = models.TextField("Description")
    read_day = models.IntegerField("")
    created_at = models.DateTimeField("", auto_now=False, auto_now_add=False)
    updated_at = models.DateTimeField("", auto_now=False)
    cover_image = models.ImageField("Cover image", upload_to='books/', blank=True, null=True)