from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    # ログイン／ログアウト／サインアップ
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # ログアウト後はログインページへリダイレクト
    path('logout/', auth_views.LogoutView.as_view(next_page='/accounts/login/'), name='logout'),
    path('signup/', views.signup, name='signup'),
]