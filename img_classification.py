# -*- coding: utf-8 -*-
"""
Created on Mon May 24 16:25:31 2021

@author: Siranjeevi
"""
import tensorflow as tf
from tensorflow import keras
import cv2
from PIL import Image, ImageOps
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input

def teachable_machine_classification(img, weights_file):
    
    np.set_printoptions(suppress=True)
    
    model = tf.keras.models.load_model('model.h5')
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image1 = img
    size = (224, 224)
    image1 = ImageOps.fit(image1, size, Image.ANTIALIAS)
    #image_array = image_array/255
    #image_array = image1.img_to_array(image)
    x = np.expand_dims(image1, axis=0)
    #normalizing_image_array = (image_array.astype(np.float32) / 127.0) -1
    image_data = preprocess_input(x)
    data[0] = image_data
    
    prediction = np.argmax(model.predict(data), axis = 1)
    return prediction