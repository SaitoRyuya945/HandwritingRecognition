import numpy as np
import matplotlib.pyplot as plt
import cv2
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
from tensorflow.keras.preprocessing.image import load_img, img_to_array, array_to_img
from PIL import Image, ImageOps

model = models.load_model("manager/static/manager/deepmodel/mnistraining.h5")
# def static_load():
#     model = models.load_model("manager/static/manager/deepmodel/mnistraining.h5")
#     return s


class TfHandWritingRecognize():
    
    def __init__(self, model_name):
        self.model = models.load_model("manager/static/manager/deepmodel/"+model_name)
        self.w1 = self.model.layers[0].get_weights()[0]
        self.w2 = self.model.layers[2].get_weights()[0]
        self.model_filter()

    def model_filter(self):
        # w = model.layers[0].get_weights()[0]
        fig = plt.figure(figsize=(10, 10))
        for i in range(64):
            plt.subplot(8, 8, i + 1)
            plt.xticks([])
            plt.yticks([])
            plt.grid(False)
            plt.imshow(self.w1[:, :, 0, i].reshape(3, 3), cmap=plt.cm.binary)
        fig.savefig("manager/static/manager/media/conv2_1.png")
        plt.clf()
        # w = model.layers[2].get_weights()[0]
        fig = plt.figure(figsize=(10, 10))
        for i in range(32):
            plt.subplot(8, 8, i + 1)
            plt.xticks([])
            plt.yticks([])
            plt.grid(False)
            plt.imshow(self.w2[:, :, 0, i].reshape(3, 3), cmap=plt.cm.binary)
        fig.savefig("manager/static/manager/media/conv2_2.png")

    def hw_predict(self, img_name):
        Xt = []
        img = load_img("manager/static/manager/media/"+img_name, grayscale=True, target_size=(28, 28))
        img = ImageOps.invert(img)
        img = img_to_array(img)
        img.shape
        print(img.shape)
        Xt.append(img)
        Xt = np.array(Xt) / 255
        # plt.imshow(img)
        # print(img.shape, Xt.shape)
        test_predicts = model.predict(Xt)
        test_predicts = np.argmax(test_predicts, axis=1)
        # print('結果：', test_predicts)
        return test_predicts[0]


class Tf49HandWritingRecognize():
    jp_hiragana = ["あ","い","う","え","お","か","き","く","け","こ","さ","し","す","せ","そ","た","ち","つ","て","と","な","に","ぬ","ね","の","は","ひ","ふ","へ","ほ","ま","み","む","め","も","や","ゆ","よ","ら","り","る","れ","ろ","わ","ゐ","ゑ","を","ん"]

    def __init__(self, model_name):
        self.model = models.load_model("manager/static/manager/deepmodel/" + model_name)
        self.w1 = self.model.layers[0].get_weights()[0]
        self.w2 = self.model.layers[2].get_weights()[0]
        # self.model_filter()

    def model_filter(self):
        # w = model.layers[0].get_weights()[0]
        fig = plt.figure(figsize=(10, 10))
        for i in range(64):
            plt.subplot(8, 8, i + 1)
            plt.xticks([])
            plt.yticks([])
            plt.grid(False)
            plt.imshow(self.w1[:, :, 0, i].reshape(3, 3), cmap=plt.cm.binary)
        fig.savefig("manager/static/manager/media/conv2_1_49.png")
        plt.clf()
        # w = model.layers[2].get_weights()[0]
        fig = plt.figure(figsize=(10, 10))
        for i in range(32):
            plt.subplot(8, 8, i + 1)
            plt.xticks([])
            plt.yticks([])
            plt.grid(False)
            plt.imshow(self.w2[:, :, 0, i].reshape(3, 3), cmap=plt.cm.binary)
        fig.savefig("manager/static/manager/media/conv2_2_49.png")

    def hw_predict(self, img_name):
        Xt = []
        img = load_img("manager/static/manager/media/" + img_name, grayscale=True, target_size=(28, 28))
        # img = ImageOps.invert(img)
        img = img_to_array(img)
        img.shape
        print(img.shape)
        Xt.append(img)
        Xt = np.array(Xt) / 255
        # plt.imshow(img)
        # print(img.shape, Xt.shape)
        test_predicts = self.model.predict(Xt)
        test_predicts = np.argmax(test_predicts, axis=1)
        # print('結果：', test_predicts)
        return test_predicts[0]

    def predictTochar(self, predict_num):

        return self.jp_hiragana[predict_num]


#モデルのフィルターの種類を表示している
def model_predict():
    # model = static_load()

def static_load():
    s = models.load_model("manager/static/manager/deepmodel/mnistraining.h5")
    return s

def model_predict():
    model = static_load()
    w = model.layers[0].get_weights()[0]
    fig = plt.figure(figsize=(10,10))
    for i in range(64):
        plt.subplot(8,8,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(w[:,:,0,i].reshape(3,3), cmap=plt.cm.binary)
    fig.savefig("manager/static/manager/media/conv2_1.png")
    plt.clf()
    w = model.layers[2].get_weights()[0]
        plt.imshow(w[:,:,0,i].reshape(3,3), cmap =
                plt.cm.binary)
    fig.savefig("manager/static/manager/deepmodel/conv2_1.png")

    w = model.layers[0].get_weights()[0]
    fig = plt.figure(figsize=(10, 10))
    for i in range(32):
        plt.subplot(8, 8, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(w[:, :, 0, i].reshape(3, 3), cmap=plt.cm.binary)
    fig.savefig("manager/static/manager/media/conv2_2.png")
    