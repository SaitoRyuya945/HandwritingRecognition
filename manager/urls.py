# managerの中でビューのURLの設定などをここに記述する。
# これをプロジェクトのurl.pyにインクルードさせることでURLを反映させる
from django.urls import path
from manager import views

app_name = 'manager'

urlpatterns = [
    # 書籍
    path('book/', views.book_list(), name='book_list'),     # 一覧
]