## Djangoのプロジェクトのセットアップ
### 参考資料
- (公式)https://docs.djangoproject.com/ja/3.0/intro/tutorial01/
- (Qiita)https://qiita.com/gragragrao/items/373057783ba8856124f3
- (Qiita)https://qiita.com/kaki_k/items/7b178ad39394a031b50d
- (js外部ファイル読み込み)https://qiita.com/t-iguchi/items/20dc31d5e004d7145634
- (jsキャンバス画像変換)https://syncer.jp/javascript-reference/canvas-todataurl
- (jQueryのpostについて)https://javascript.programmer-reference.com/jquery-jquery-post/
- (PythonBase64をエンコードする)http://motojapan.hateblo.jp/entry/2017/12/19/112544
### 必要なパッケージ
 
```
pip install django
pip install django-bootstrap4
pip install 
```
#### プロジェクトの作り方
ワークスペースに移動し、以下のコマンドを入力する

```
django-admin startproject HandwriteingRecoginition(プロジェクト名)
python manage.py startapp manager(アプリ名)
```

こうすることで色々ファイルが作成されるが、
主に扱うファイルが決まっている。
パスや細々した設定については

```
HandwriteingRecoginition/
    settings.py   //プロジェクトの設定ファイル
    urls.py       //プロジェクトのURL宣言、目次に当たるもの
    mangae.py     //プロジェクトの操作コマンドを行うためのユーティリティ
```
開発では

```
manager/
    models.py     //データベースのデータモデルの定義など
    view.py       //ビューごとの処理などを定義できる
```

を主に利用していく。

#### アプリを追加する
```
settings.py/
...
   INSTALLED_APPS = [
    ...
    # 新しく追加
    'manager.apps.ManagerConfig',   # managerアプリケーションの追加
    'bootstrap4',                   # django-bootstrap4の追加
] 
```

#### データベースをマイグレートする

```
python manage.py makemigrations manager     # 
python manage.py migrate    # models.pyのデータベースモデルを定義しなおすたびに行う

# どのようなSQLになるか確認できる
python manage.py sqlmigrate manager 0001

```

#### 管理者用アカウントの作成

```
python manage.py createsuperuser
ユーザ名: ----------
メールアドレス: ------@----
Password: hogehoge
Password (again): hogehoge
```
これでrunserverでアクセスするURL+/admin/から管理者画面にアクセスできる

#### サーバを起動する
```
python manage.py runserver
```
これで指定したURLにアクセスすることでサイトを閲覧できる
止める時は Ctrl＋C 

