# WSGI 設定パッチ適用手順

以下の手順を、小学生にも分かるように説明します。

1. PythonAnywhere にログインして、Bash コンソールを開く  
   - 「Consoles」タブ → 「Start a new console」→ 「Bash」を選択

2. WSGI ファイルがあるフォルダに移動する  
   ```
   cd /var/www
   ```

3. 先ほど移動したパッチファイルを使って、WSGI 設定を修正する  
   ```
   patch griko_pythonanywhere_com_wsgi.py < ~/portfolio/docs/WSGI_PATCH.diff
   ```  
   - `patch` コマンドは元のファイルを書き換える命令  
   - パッチファイルは `~/portfolio/01_URLDispatch/first_project/docs/WSGI_PATCH.diff` にあります  
   - このコマンドを `/var/www` フォルダ内で実行すると、WSGI ファイルの先頭が修正されます

4. Web アプリをリロードして変更を反映する  
   ```
   pa_reload webapp
   ```  
   - 新しい設定がサーバーに読み込まれます  
   - 「pa_reload」はウェブアプリの再読み込みボタンを押すイメージです

5. エラーが消えたか確認する  
   - ブラウザで本番サイトを開き、ログイン/ログアウトや映画一覧ページを表示  
   - エラーが出なければ成功です

以上の手順で、WSGI 周りのエラーが解消できます。