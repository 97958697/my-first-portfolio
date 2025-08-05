# first_project

## 概要
Djangoベースの映画レビューアプリケーションです。  
ユーザー登録・ログイン機能を備え、スタッフユーザーは映画の登録・編集・削除が可能です。  
一般ユーザーは映画のレビュー投稿・編集・削除が行えます。

## 機能一覧
- カスタムユーザーモデル（`AbstractUser`継承）
- 映画モデル (`Movie`): タイトル、説明、ポスター画像、公開日
- レビューモデル (`Review`): ユーザー・映画の外部キー、評価（1～5）、コメント、一意制約
- ムービー一覧・詳細・追加・編集・削除（スタッフユーザーのみ）
- レビュー投稿・編集・削除（ログインユーザーのみ）
- 静的ファイル（CSS）およびメディアファイル（画像）管理
- 単体テスト（モデル制約、フォームバリデーション、ビュー挙動）

## 環境構築

1. リポジトリをクローン  
   ```
   git clone <リポジトリURL>
   cd portfolio/01_URLDispatch/first_project
   ```

2. 仮想環境の作成・有効化  
   Windows (PowerShell):
   ```
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
   macOS/Linux:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. 依存パッケージのインストール  
   ```
   pip install -r requirements.txt
   ```

4. マイグレーション実行  
   ```
   python manage.py migrate
   ```

5. 管理ユーザーの作成 (スタッフ権限)  
   ```
   python manage.py createsuperuser
   ```

## 実行方法

開発用サーバー起動:
```
python manage.py runserver
```
ブラウザで `http://127.0.0.1:8000/` にアクセス

## テスト実行

```
python manage.py test
```
