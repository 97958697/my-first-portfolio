from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    # ログイン／ログアウト／サインアップ
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # ログアウト後は映画一覧にリダイレクト
    path('logout/', auth_views.LogoutView.as_view(next_page='movie_list'), name='logout'),
    path('signup/', views.signup, name='signup'),
]