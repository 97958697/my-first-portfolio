from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, get_user_model

class CustomAuthenticationForm(AuthenticationForm):
    """
    AuthenticationForm を継承し、
    ユーザー名の存在チェックとパスワード検証を行って
    フィールドごとのエラーを設定する Form。
    """
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        UserModel = get_user_model()
        # ユーザー存在チェック
        if username and not UserModel.objects.filter(username=username).exists():
            self.add_error('username', '該当するユーザーが存在しません。')
            return self.cleaned_data
        # パスワード検証
        user = authenticate(self.request, username=username, password=password)
        if username and password and user is None:
            self.add_error('password', 'パスワードが正しくありません。')
            return self.cleaned_data
        return super().clean()