from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.http import HttpResponse

from manager.models import Book
from datetime import datetime

# 自作フォームの定義
from . import forms


class HandRecognize(TemplateView):
    template_name = "imgput.html"

    def get(self, request, *args, **kwargs):
        """画像送信前ページ"""
        context = super(HandRecognize, self).get_context_data(**kwargs)     # htmlにdjangoで値を渡してあげることに使う
        context['page_name'] = "手書き文字認識マン"
        context['date'] = int(datetime.now().strftime('%Y%m%d%H%M%S'))      # 日付
        context['form'] = forms.UploadFileForm

        return render(self.request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """画像送信後ページ"""
        context = super(HandRecognize, self).get_context_data(**kwargs)     # htmlにdjangoで値を渡してあげることに使う
        context['page_name'] = "手書き文字認識マン"
        context['date'] = int(datetime.now().strftime('%Y%m%d%H%M%S'))      # 日付
        context['form'] = forms.UploadFileForm

        return render(self.request, self.template_name, context)


def book_list(request):
    """書籍の一覧"""
    # return HttpResponse('書籍の一覧')
    books = Book.objects.all().order_by('id')
    return render(request,
                  'index.html',     # 使用するテンプレート
                  {'books': books})         # テンプレートに渡すデータ


def book_edit(request, book_id=None):
    """書籍の編集"""
    return HttpResponse('書籍の編集')


def book_del(request, book_id):
    """書籍の削除"""
    return HttpResponse('書籍の削除')