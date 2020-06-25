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
    # s = models.load_model("../static/manager/deepmodel/mnistraining.h5")
    s = models.load_model("./static/manager/deepmodel/mnistraining.h5")

    # a = models.load_model("static/manager/deepmodel/mnistraining.h5")







