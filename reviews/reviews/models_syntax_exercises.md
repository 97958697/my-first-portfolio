# models.py 文法とルールの穴埋め練習

以下は `reviews/models.py` に出てくるコードの一部です。空欄に当てはまるキーワードや名前を埋めてみましょう！

```python
# 1. Django ORM 用のモデル基底クラスを読み込む
from django.db import models  # DjangoのORMでモデル定義を行うときに使う

# 2. ユーザーモデルを拡張するクラス定義
class User(AbstractUser):  #Django標準のユーザー設計図を拡張するベースクラス
    pass

# 3. 複数ユーザー ↔ 複数グループの関係を作るフィールド
groups = models.ManyToManyField(  #複数のオブジェクト間の多対多の関係を定義するフィールド
    'auth.Group',
    related_name='reviews_user_groups',
    blank=True,
)

# 4. 一対多の関係を作る外部キーフィールド
movie = models.ForeignKey(  # 他モデルへの一対多の外部キーを定義するフィールド
    Movie,
    on_delete=models.PROTECT,
    related_name='reviews',
)

# 5. 数値範囲チェック用に 1〜5 だけ許可するバリデータ
rating = models.PositiveSmallIntegerField(
    validators=[MinValueValidator(1), MaxValueValidator(5)]
)

# 6. データを自動でテーブルに保存する日時フィールド（作成日時）
created_at = models.DateTimeField(auto_now_add=True)  #レコード作成日時を自動記録するフィールド

# 7. モデルの追加設定を書くクラス名
class Meta:  #モデルの追加設定（メタデータ）を定義する内部クラス
    ordering = ['-created_at']

# 8. ユニーク制約を追加する機能
constraints = [
    models.UniqueConstraint(  #指定したフィールドに一意制約を追加する機能
        fields=['user', 'movie'],
        name='unique_user_movie_review'
    )
]

# 9. オブジェクトを文字列化するときに呼ばれるメソッド
def __str__(self):  #オブジェクトを文字列化して表示する際に呼び出される特殊メソッド
    return f'{self.user.username} → {self.movie.title} ({self.rating})'