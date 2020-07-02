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


def model_predict():
    # model = static_load()
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
    fig = plt.figure(figsize=(10, 10))
    for i in range(32):
        plt.subplot(8, 8, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(w[:, :, 0, i].reshape(3, 3), cmap=plt.cm.binary)
    fig.savefig("manager/static/manager/media/conv2_2.png")


def predicts():
    Xt = []
    img = load_img("manager/static/manager/media/input.png", grayscale=True, target_size=(28, 28))
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
