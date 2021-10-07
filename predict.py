#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 18:45:05 2020

@author: sudhanshukumar
"""

import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

class dogcat:
    def __init__(self,filename):
        self.filename =filename


    def predictiondogcat(self):
        # load model
        model = load_model('VGG16_Garbage_Model_2021_10_05_20_08_56_.h5')

        # summarize model
        # print(model.summary())
        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = model.predict(test_image)

        result = result.flatten()

        if result[0] == 1:
            prediction = 'Battery'
            return [{ "image" : prediction}]
        elif result[1] == 1:
            prediction = 'biological'
            return [{ "image" : prediction}]
        elif result[2] == 1:
            prediction = 'Brown Glass'
            return [{ "image" : prediction}]
        elif result[3] == 1:
            prediction = 'cardboard'
            return [{ "image" : prediction}]
        elif result[4] == 1:
            prediction = 'Clothes'
            return [{ "image" : prediction}]
        elif result[5] == 1:
            prediction = 'Green Glass'
            return [{ "image" : prediction}]
        elif result[6] == 1:
            prediction = 'Metal'
            return [{ "image" : prediction}]
        elif result[7] == 1:
            prediction = 'Paper'
            return [{ "image" : prediction}]
        elif result[8] == 1:
            prediction = 'Plastic'
            return [{ "image" : prediction}]
        elif result[9] == 1:
            prediction = 'Shoes'
            return [{ "image" : prediction}]
        elif result[10] == 1:
            prediction = 'Trash'
            return [{ "image" : prediction}]
        elif result[11] == 1:
            prediction = 'White Glass'
            return [{ "image" : prediction}]


