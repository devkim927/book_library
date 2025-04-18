from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm,CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
User = get_user_model()


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 회원가입 후 자동 로그인
            return redirect('books:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html', {'user': request.user})

@login_required
def update_view(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'accounts/update.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('books:index')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()  # 인증된 사용자
            login(request, user)  # 세션 시작
            return redirect('accounts:profile')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def user_profile(request, user_pk):
    profile_user = get_object_or_404(User, pk=user_pk)
    return render(request, 'accounts/user_profile.html', {'profile_user': profile_user})

@login_required
def follow_toggle(request, user_pk):
    target_user = get_object_or_404(User, pk=user_pk)

    if request.user == target_user:
        return redirect('accounts:user_profile', user_pk)

    if target_user in request.user.followings.all():
        request.user.followings.remove(target_user)  # 언팔로우
    else:
        request.user.followings.add(target_user)     # 팔로우

    return redirect('accounts:user_profile', user_pk)