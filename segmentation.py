import streamlit as st
from PIL import Image
import numpy as np
from tensorflow import keras
from keras.models import load_model
from keras import backend as K 
import cv2


st.title('My first app')

st.title("Segmentation  with Dense-UNet")


@st.cache(allow_output_mutation=True)
def load_model():
    model = load_model("satellitesegment.h5")
    session = K.get_session()
    return model,session


@st.cache(allow_output_mutation=True)
def predict(model,img):
    img_npy = cv2.imread(img)
    result_img = model.predict(img_npy)
    result_img = result_img[:,:,:,0]>0.5
    result_img = Image.fromarray(result_img)
    return result_img


uploaded_file = st.file_uploader("Choose an image...", type="tif")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

button = st.button('Predict')

if button:
    t = st.empty()
    t.markdown('## İmage is segmenting...')
    model, session = load_model()
    model,session = load_model()
    image = image.reshape((1,512,512,3))
    K.set_session(session)
    result_img = predict(model,image)
    t.markdown('## Segmentation result:')
    st.image(result_img, caption='Predicted Image.', use_column_width=True)
