from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.http import HttpResponse

from manager.models import Book
from datetime import datetime

# 自作フォームの定義
from . import forms
from django.template.context_processors import csrf
import sys
# Base64関連の処理
import base64
import PIL
from PIL import Image
from io import BytesIO

class HandRecognize(TemplateView):
    template_name = "imgput.html"

    def get(self, request, *args, **kwargs):
        """画像送信前ページ"""
        context = super(HandRecognize, self).get_context_data(**kwargs)     # htmlにdjangoで値を渡してあげることに使う
        context['page_name'] = "手書き文字認識マン"
        context['date'] = int(datetime.now().strftime('%Y%m%d%H%M%S'))      # 日付
        # context['form'] = forms.UploadFileForm
        context['message'] = forms.UserForm(label_suffix=' : ')

        return render(self.request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """画像送信後ページ"""
        print("post通信")
        context = super(HandRecognize, self).get_context_data(**kwargs)     # htmlにdjangoで値を渡してあげることに使う
        context['page_name'] = "手書き文字認識マン"
        context['date'] = int(datetime.now().strftime('%Y%m%d%H%M%S'))      # 日付
        # context['form'] = forms.UploadFileForm
        # print(request.POST['areaone'])
        # context['form'] = request.POST['message']
        # context['message'] = request.POST['message']
        img_data = request.POST['image']
        print(type(img_data))
        base64_to_image(img_data)
        # if forms.is_valid():
        # print("ファイル")
        # handle_uploaded_file(request.FILES['image'])
        # file_obj = request.FILES['image']
        # context.update(csrf(request))
        return render(self.request, self.template_name, context)


def base64_to_image(base_64: str):
    print('#############start')
    a = base_64.split(',')[1]
    decoded = base64.b64decode(a)
    img = Image.open(BytesIO(decoded))
    img.save('manager/static/manager/media/input.png')
    print('#############end')


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


# ------------------------------------------------------------------
def handle_uploaded_file(file_obj):
    sys.stderr.write("*** handle_uploaded_file *** aaa ***\n")
    sys.stderr.write(file_obj.name + "\n")
    # file_path = 'static/media/' + file_obj.name
    file_path = 'static/manager/media' + 'input.png'
    # sys.stderr.write(file_path + "\n")
    with open(file_path, 'wb+') as destination:
        for chunk in file_obj.chunks():
            # sys.stderr.write("*** handle_uploaded_file *** ccc ***\n")
            destination.write(chunk)
            # sys.stderr.write("*** handle_uploaded_file *** eee ***\n")

#
# ------------------------------------------------------------------