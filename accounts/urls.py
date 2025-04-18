from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView


app_name = 'accounts'
urlpatterns = [
    path("login/", views.login_view, name="login"),
    path('logout/', views.logout_view, name='logout'),
    path("signup/", views.signup_view, name="signup"),
    path("profile/", views.profile_view, name="profile"),
    path("update/", views.update_view, name="update"),
    path('profile/<int:user_pk>/', views.user_profile, name='user_profile'),
    path('follow/<int:user_pk>/', views.follow_toggle, name='follow_toggle'),
]
