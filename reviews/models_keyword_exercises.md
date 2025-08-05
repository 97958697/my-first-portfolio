# models.py キーワード演習問題

以下は `reviews/models.py` の一部です。空欄にキーワードを埋めて、基本的な文法を覚えましょう！

```python
# 1. Django ORM 用の models モジュールを読み込む
from django.db import _____

# 2. AbstractUser を継承して User クラスを定義する
class User(_____):
    pass

# 3. モデルの文字列表現を定義する special メソッド
____ __str__(self):
    return f'{self.username}'

# 4. メソッド内で値を返すときに使うキーワード
def get_username(self):
    _____ self.username

# 5. f-string を使うには、文字列リテラルの先頭にこの文字をつけよう
message = _____'User: {self.user.username}'

# 5. 何もしない空のコードを書きたいときに使うキーワード
    _____