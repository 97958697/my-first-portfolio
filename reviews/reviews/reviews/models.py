# Rooさん補足: このファイルは Django のモデルを定義してるよ。ざっくり言うと、
# データベースのテーブルを Python のクラスで設計図みたいに書く感じだよ〜
from django.db import models  # Roo: Django の ORM を使うためのモデル基底クラス
# Rooさん補足: ORMはコンピュータと言葉が違うデータベースと会話する通訳みたいなもので、  
# Pythonのクラスを書くと勝手に「この形で保存してね」「これを読み込んでね」とやってくれる魔法の仕組みだよ🪄
# Rooさん補足: 「models」って名前は、Pythonのクラスを使ってデータベースのテーブルをサクッと作れる
# 魔法の道具セットのことなんだ～。「これ書いたら勝手にテーブルできるよ！」って感じ😊
# Rooさん補足: ここでは Django のモデルを定義してるよ！データベースのテーブルを Python のクラスで設計図みたいに書く感じだよ〜
from django.contrib.auth.models import AbstractUser, Group, Permission  # Roo: ユーザー認証・権限まわりをカスタマイズするために使う
from django.conf import settings  # Roo: AUTH_USER_MODEL を参照するのに必要
from django.core.validators import MinValueValidator, MaxValueValidator  # Roo: 評価値の範囲チェック用バリデータ
# Rooさん補足: django.contrib.auth.models は「ユーザーのログインや権限まわり」の部品が入った宝箱だよ！
# ・AbstractUser は「最初から用意されたユーザー設計図」だから、ログイン機能をパパッと使いたいときに便利😊
# ・Group は「この人はどのグループ(仲間)に所属しているか」を管理するノートみたいなもの📝
# ・Permission は「この人にどんな操作を許可するか」を決めるチケット券売機みたいな仕組みだよ🎟️
# Rooさん補足: django.conf.settings はアプリ全体の設定情報がギュッと詰まった箱！
# 「どのユーザーモデルを使う？」「データベースはどこ？」など、大切なルールを覚えておいてくれるよ📦
# Rooさん補足: django.core.validators はデータの正しさチェック道具箱🔧
# ・MinValueValidator は「これ以上の数字じゃないとダメ！」をチェック、
# ・MaxValueValidator は「これ以下の数字じゃないとダメ！」をチェックしてくれる魔法の仕組みだよ🪄
# Rooさん補足: ここは User クラスの定義スタート！ユーザー情報を扱うところだから「こんな感じでログイン情報とか持ってるんだよ〜」ってイメージしてね😊
# Rooさん追記: ここからはユーザーの情報（ログインユーザーとか）を扱うクラスだよ！何ができるか想像してみよう～
class User(AbstractUser):
# Rooさん補足: groupsは「このユーザーがどのグループに所属しているか」を記録するところ！例えると、趣味のクラブやサークルを登録するイメージだよ〜
# Rooさん補足: 将来フィールド追加などの拡張ができるようにしています。
# Roo: Group／Permission モデルをオーバーライドして related_name を変更
# これによって逆参照時の名前衝突を回避します。
# Rooさん補足: 「モデルをオーバーライドする」っていうのは、もともとある設計図（モデル）に自分のルールをポンッと上書きしてカスタマイズするイメージだよ〜  
# 例えば先生がくれた宿題プリントに自分のメモを追記するような感じで、元の機能をのこしつつ必要なところだけ変えられる魔法みたいな仕組みなんだ🎨
# Rooさん補足: 例えば同じ名前のお友達がいても、related_nameを変えると
# 教室ごと（グループごと）に区別して呼べるイメージだよ😊
    # 関連: [`01_URLDispatch/first_project/reviews/migrations/0001_initial.py:52`]
    groups = models.ManyToManyField(
        'auth.Group',  # Rooさん補足: ManyToManyField は「多対多」の関係を作る魔法！  
# ユーザーは複数のグループに入れるし、グループにはたくさんのユーザーが入れるよ。  
# Rooさん補足: 中間テーブルは電話帳みたいな存在だよ📒  
# 「誰がどのグループに入ったか」を一行ずつ記録して、  
# ユーザー ↔ グループ のつながりを管理してくれる名簿なんだ😊
# Django が裏で「中間テーブル」という名簿を自動で作ってくれるんだ😊
# Rooさん補足: 'auth.Group' は Django が最初から用意してくれている「グループ情報の設計図」を指しているよ！学校で言うと「クラス名簿のひな形」を使うイメージ😊
# Rooさん補足: user_permissionsは「このユーザーに追加で与えたい特別な権限」を登録する場所だよ。例えば「記事を書く権限」や「管理画面に入る権限」をイメージしてみてね😊
        related_name='reviews_user_groups',  # Roo: 標準の related_name と衝突しないようにする
        blank=True,
        help_text='The groups this user belongs to.',  # Rooさん補足: 管理画面でこのフィールドの説明テキストとして表示されるよ！
# Rooさん補足: この “The groups this user belongs to.” は管理画面で表示される「説明文」のことだよ！
# Rooさん補足: “belongs to” は「〜に属している」という意味だよ！  
# 「どのグループに入っているか」をやさしく教えてくれるメッセージで、初めての人にも分かりやすくなるように書かれているんだ😊
        verbose_name='groups',  # Rooさん補足: 管理画面でのラベル名として使われるよ
# Rooさん補足: “verbose” は「詳細な」という意味で、verbose_name は「管理画面などで表示するときに見やすく、くわしく書かれた名前」を指定するオプションなんだよ😊
    )
    # 関連: [`01_URLDispatch/first_project/reviews/migrations/0001_initial.py:53`]
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='reviews_user_permissions',  # Roo: 同様に権限の逆参照名をユニークに
        blank=True,
        help_text='Specific permissions for this user.',
# Rooさん補足: [`help_text='Specific permissions for this user.'`](01_URLDispatch/first_project/reviews/models.py:73) の “Specific” は「特定の」「個別の」という意味で、グループの権限とは別に、このユーザーだけに与える特別な権限をわかりやすく表した言葉なんだよ😊
        verbose_name='user permissions',
# Rooさん補足: ここからは「いつ作ったか」「いつ更新したか」を自動で覚えてくれるクラスだよ！地味だけど、とっても便利なんだ😊
    )
# Rooさん補足: TimeStampedModel は「作成日時」と「更新日時」を自動で覚えてくれる便利クラスだよ！
# Rooさん補足: TimeStampedModel は「いつ作ったか」「いつ更新したか」を自動で記録してくれる便利クラスだよ！
class TimeStampedModel(models.Model):
# Rooさん補足: Roo: created_at と updated_at を自動的に設定する
# Rooさん補足: 抽象基底クラスです。これを継承すると全モデルで日時管理ができる。
    # 関連: [`01_URLDispatch/first_project/reviews/migrations/0001_initial.py:26`]
    created_at = models.DateTimeField(auto_now_add=True)
    # Roo: オブジェクト生成時刻を自動設定
    # 関連: [`01_URLDispatch/first_project/reviews/migrations/0001_initial.py:27`]
    updated_at = models.DateTimeField(auto_now=True)
    # Roo: オブジェクト保存時に更新時刻を自動設定
# Rooさん補足: [`class Meta:`](01_URLDispatch/first_project/reviews/models.py:91) は「モデルの追加設定を書く特別な箱」のことだよ！メタデータ（モデルに関する情報）をここにまとめることで、テーブル名や並び順、抽象モデルかどうかなど、データベースに伝える設定を分かりやすく整理できるんだ😊
    # 関連: [`01_URLDispatch/first_project/reviews/migrations/0001_initial.py:25`]  ← TimeStampedModel の抽象設定はマイグレーション非出力
    class Meta:
# Rooさん補足: ここからMovieクラス！映画のタイトルや説明、画像、公開日を持たせてるよ。アプリで映画一覧を表示するときに使うんだ～
        abstract = True  # Roo: テーブル化せず、継承先にフィールドだけ継承する設定
class Movie(TimeStampedModel):
# Rooさん補足: Roo: 映画情報を格納するモデル。
# Rooさん補足: TimeStampedModel を継承して作成/更新日時を持つ。
    # 関連: [`01_URLDispatch/first_project/reviews/migrations/0001_initial.py:28`]
    title = models.CharField(max_length=255)
    # Roo: 映画タイトルは最大 255 文字のテキストフィールド
    # 関連: [`01_URLDispatch/first_project/reviews/migrations/0001_initial.py:29`]
    description = models.TextField()
    # Roo: 映画のあらすじや詳細説明を格納
    # 関連: [`01_URLDispatch/first_project/reviews/migrations/0001_initial.py:30`]
    image = models.ImageField(
        upload_to='movies/%Y/%m/%d/',  # Roo: 画像ファイルは日付フォルダーで整理
        blank=True,
        null=True
    )
    # Roo: 画像なしも許容する設定
    # 関連: [`01_URLDispatch/first_project/reviews/migrations/0001_initial.py:31`]
    release_date = models.DateField(blank=True, null=True)
    # Roo: 公開日は任意入力
    # 関連: [`01_URLDispatch/first_project/reviews/migrations/0001_initial.py:54`]  ← Movie モデルの ordering/indexes がこの行で反映
    class Meta:
        ordering = ['-release_date', 'title']
        # Roo: 公開日の新しい順、同日にタイトル順でソートされる
        indexes = [
            models.Index(fields=['-release_date']),
            # Roo: ソートキーにインデックスを貼って高速化
# Rooさん補足: 「インデックス」は本の巻末にある「索引」のようなものだよ😊 例えば本である言葉を探すとき、巻末の索引を見ればパッとページがわかるよね。同じようにデータベースにインデックスをつけると、ソートや検索のときに必要なデータをすばやく見つけられるから「高速化」できるんだ！
        ]
    # 関連: 管理画面/list_display でタイトル表示 ([`templates/mock_index.html:12`])
    def __str__(self):
        # Roo: オブジェクトを文字列化するときにタイトルを返すので管理画面で見やすい
        return self.title
class Review(TimeStampedModel):
    # Rooさん補足:同じユーザーが同じ映画に二重投稿しないように制約を入れ、評価を 1〜5 のバリデーションでチェックします。
    # 関連: [`01_URLDispatch/first_project/reviews/migrations/0001_initial.py:73`]
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,  # Roo: ユーザー削除時はレビューも削除
        related_name='reviews'
    )
    # Roo: レビュー投稿者。AUTH_USER_MODEL を使うとカスタムモデル名に依存しない
    # 関連: [`01_URLDispatch/first_project/reviews/migrations/0001_initial.py:72`]
    movie = models.ForeignKey(
        Movie,
        on_delete=models.PROTECT,  # Roo: 映画が削除されない限りレビューは保護
        related_name='reviews'
    )
    # Roo: レビュー対象の映画
    # 関連: [`01_URLDispatch/first_project/reviews/migrations/0001_initial.py:70`]
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
        # Roo: レーティングは 1～5 の数値のみ許可
    )
    # 関連: [`01_URLDispatch/first_project/reviews/migrations/0001_initial.py:71`]
    comment = models.TextField(blank=True)
    # Roo: 任意コメントは空文字 OK
    # 関連: [`01_URLDispatch/first_project/reviews/migrations/0001_initial.py:90`]  ← Review モデルの制約・ordering/indexes 出力箇所
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'movie'],
                name='unique_user_movie_review'
            )
            # Roo: 同一ユーザー・同一映画での重複投稿を防ぐ
        ]
        ordering = ['-created_at']
        # Roo: 新しい順に表示
        indexes = [
            models.Index(fields=['-created_at']),
            # Roo: ソートの高速化用インデックス
        ]
    # 関連: テンプレート ([`templates/mock_detail.html:5`]) で「ユーザー → 映画タイトル (評価)」表示
    def __str__(self):
        # Roo: 「ユーザー → 映画タイトル (評価)」形式で分かりやすく文字列に変換
        return f'{self.user.username} → {self.movie.title} ({self.rating})'