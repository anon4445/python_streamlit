from PIL import Image
import streamlit as st

uploaded_file = st.file_uploader("Choose an image...", type=['jpeg', 'png', 'jpg'])
if st.button("click me"):
    img = Image.open(uploaded_file)
    st.image(img ,use_column_width=True)
    grayscale_image = img.convert('L')
    st.image(grayscale_image ,use_column_width=True)