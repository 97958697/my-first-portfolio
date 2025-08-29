from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import LogoutGetView
from .forms import CustomAuthenticationForm

app_name = 'accounts'

urlpatterns = [
    # ログイン／ログアウト／サインアップ
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html', form_class=CustomAuthenticationForm), name='login'),
    # ログアウト後はログインページへリダイレクト
    path('logout/', LogoutGetView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]