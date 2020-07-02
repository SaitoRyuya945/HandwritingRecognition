# -*- coding: utf-8 -*-
"""
Created 2020/06/15 20:03:11

@author: okuyama.takahiro
@author: okuyama.takahiro
@author: okuyama.takahiro
@author: okuyama.takahiro
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2
import tensorflow as tf
from tensorflow.keras import datasets, layers, models

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
        plt.imshow(w[:, :, 0, i].reshape(3, 3), cmap=
        plt.cm.binary)
    fig.savefig("manager/static/manager/deepmodel/conv2_2.png")
