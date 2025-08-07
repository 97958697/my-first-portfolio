# テスト内変数の穴埋め演習

以下は `reviews/tests.py` に登場する変数（箱）の演習問題です。空欄に当てはまる変数名や値を埋めてみましょう。

```python
class ReviewModelTests(TestCase):
    def setUp(self):
        # 1. ユーザーを作成して self の箱に保存する
        self._____ = get_user_model().objects.create_user(username='bob', password='pass')
        # 2. テスト用映画を作成して self の箱に保存する
        self._____ = Movie.objects.create(title='テスト映画', release_date='2020-01-01', description='テスト用の映画です')

    def test_user_str(self):
        # 3. ユーザー名を文字列化して比較する変数
        self.assertEqual(str(self._____), 'bob')

    def test_unique_user_movie(self):
        # 4. 初回レビュー作成で使う変数
        Review.objects.create(user=self._____, movie=self._____, rating=3)
        # 5. 2回目の同じ組み合わせでエラーになるか確認する変数
        with self.assertRaises(IntegrityError):
            Review.objects.create(user=self._____, movie=self._____, rating=4)

    def test_rating_range(self):
        # 6. 不正な評価値を持つインスタンスを作成する時の変数名
        bad = Review(user=self._____, movie=self._____, rating=0)
        with self.assertRaises(ValidationError) as cm:
            bad.full_clean()
        # 7. エラー辞書に含まれるキーを確認する変数
        self.assertIn('rating', cm.exception.error_dict)

    def test_movie_ordering(self):
        # 8. 古い映画を入れる変数
        m1 = Movie.objects.create(title='古い', release_date='2000-01-01', description='')
        # 9. 新しい映画を入れる変数
        m2 = Movie.objects.create(title='新しい', release_date='2025-01-01', description='')
        # 10. クエリセットをリスト化して保存する変数
        qs = list(Movie.objects.all())
        # 11. 一番最初に来る映画は 変数名
        self.assertEqual(qs[0], _____)
        # 12. 次に来る映画は 変数名
        self.assertEqual(qs[1], _____)