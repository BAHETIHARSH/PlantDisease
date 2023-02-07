import streamlit as st
import pandas as pd
import numpy as np
from diseaseDetection import *
from prePreocess import *
from io import StringIO
import cv2
from PIL import Image


st.title('Plant Disease Detection')


# picture = st.camera_input("Take a picture")
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    st.image(uploaded_file)
    img = Image.open(uploaded_file)
    img.save("./upload.png")

    path = "./upload.png"

    data = preprocess(path)
    disease = predictDisease(data)
    st.text(f'Predicted Disease : {disease}')

