import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow import keras
import cv2
from PIL import Image, ImageOps
import numpy as np



from img_classification import teachable_machine_classification
model = load_model('model.h5')


uploaded_file = st.file_uploader("Upload an x-ray to predict disease", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded X-ray.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label = teachable_machine_classification(image, 'model.h5')
    if label == 0:
        st.write("PNEUMONIA")
    elif label == 1:
        st.write("NORMAL")
    else:
        st.wirte("COVID19")



