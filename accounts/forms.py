from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django.contrib.auth import get_user_model
from django import forms
User = get_user_model()

GENRE_CHOICES = [
    ('자연', '자연'),
    ('과학', '과학'),
    ('문학', '문학'),
    ('컴퓨터', '컴퓨터'),
    ('자기개발', '자기개발'),
    ('김홍배', '김홍배'),
]


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="비밀번호",
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label="비밀번호 확인",
        widget=forms.PasswordInput,
    )

    interests = forms.MultipleChoiceField(
        choices=GENRE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label="관심장르",
        required=False
    )

    class Meta:
        model = User
        fields = (
            'username', 'email', 'nickname', 'gender', 'age',
            'weekly_reading', 'yearly_goal', 'profile_image', 'interests',
        )
        labels = {
            'username': '아이디',
            'email': '이메일',
            'nickname': '이름',
            'gender': '성별',
            'age': '나이',
            'weekly_reading': '주간 평균 독서 시간(시간)',
            'yearly_goal': '연간 독서량(권)',
            'profile_image': '프로필 사진',
            'interests': '관심장르',
        }
        widgets = {
            'gender': forms.Select(choices=[('M', '남성'), ('F', '여성')]),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다.")
        return password2

    def clean_interests(self):
        data = self.cleaned_data.get("interests", [])
        return ",".join(data)


class CustomUserChangeForm(UserChangeForm):
    password1 = forms.CharField(
        label="새 비밀번호",
        widget=forms.PasswordInput,
        required=False
    )
    password2 = forms.CharField(
        label="새 비밀번호 확인",
        widget=forms.PasswordInput,
        required=False
    )

    interests = forms.MultipleChoiceField(
        choices=GENRE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label="관심장르",
        required=False
    )

    class Meta:
        model = User
        fields = (
            'email', 'nickname', 'gender', 'age',
            'weekly_reading', 'yearly_goal', 'profile_image', 'interests'
        )
        labels = {
            'email': '이메일',
            'nickname': '이름',
            'gender': '성별',
            'age': '나이',
            'weekly_reading': '주간 독서 시간',
            'yearly_goal': '연간 독서량',
            'profile_image': '프로필 사진',
            'interests': '관심 장르',
        }
        widgets = {
            'gender': forms.Select(choices=[('M', '남성'), ('F', '여성')]),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # interests: 문자열 → 리스트 변환
        if self.instance and self.instance.interests:
            self.initial['interests'] = self.instance.interests.split(',')

    def clean_interests(self):
        data = self.cleaned_data.get("interests", [])
        return ",".join(data)

    def clean(self):
        cleaned_data = super().clean()
        pw1 = cleaned_data.get("password1")
        pw2 = cleaned_data.get("password2")

        if pw1 or pw2:
            if pw1 != pw2:
                raise forms.ValidationError("비밀번호가 일치하지 않습니다.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        pw1 = self.cleaned_data.get("password1")

        if pw1:
            user.set_password(pw1)  # 새 비밀번호 설정

        if commit:
            user.save()
        return user

