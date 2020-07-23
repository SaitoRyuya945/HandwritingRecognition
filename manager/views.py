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

# from .mytfkeras import predicts, model_predict
from .mytfkeras import TfHandWritingRecognize
from .mytfkeras import Tf49HandWritingRecognize
import tensorflow as tf
from tensorflow.keras import datasets, layers, models


class HandRecognize(TemplateView):
    template_name = "imgput.html"
    input_name = "input.png"
    model_name = "mnistraining.h5"
    jp49model_name = "k49_ac09958.h5"

    def __init__(self):
        self.hw = TfHandWritingRecognize(self.model_name)
        self.jp49 = Tf49HandWritingRecognize(self.jp49model_name)
        self.res = 99
        # self.hw.model_filter()

    def get(self, request, *args, **kwargs):
        """画像送信前ページ"""
        context = super(HandRecognize, self).get_context_data(**kwargs)     # htmlにdjangoで値を渡してあげることに使う
        context['page_name'] = "手書き文字認識マン"
        context['date'] = int(datetime.now().strftime('%Y%m%d%H%M%S'))      # 日付
        # context['form'] = forms.UploadFileForm
        # context['message'] = forms.UserForm(label_suffix=' : ')
        context['result'] = "予測結果が入ります"
        # static_load

        return render(self.request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """画像送信後ページ"""
        print("post通信")
        context = super(HandRecognize, self).get_context_data(**kwargs)     # htmlにdjangoで値を渡してあげることに使う
        context['page_name'] = "手書き文字認識マン"
        context['date'] = int(datetime.now().strftime('%Y%m%d%H%M%S'))      # 日付
        img_data = request.POST['image']
        mode = request.POST['mode']
        base64_to_image(img_data)
        print(mode)

        # 手書き認識処理
        # mode=0の時は数字予測,1の時はひらがな予測
        if mode == "0":
            self.res = self.hw.hw_predict(self.input_name)
            self.res = str(self.res)
            print(self.res)

        else:
            self.res = self.jp49.hw_predict(self.input_name)
            print(self.res)
            self.res = self.jp49.predictTochar(self.res)
            print(self.res)

        context['result'] = "5です"

        return HttpResponse("予測結果: "+self.res)
        # return render(self.request, self.template_name, context)


class Predicted(TemplateView):
    template_name = "result.html"

    def get(self, request, *args, **kwargs):
        """レイヤー表示ページ"""
        context = super(Predicted, self).get_context_data(**kwargs)     # htmlにdjangoで値を渡してあげることに使う
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