import streamlit as st
import numpy as np
from PIL import Image

st.set_page_config(page_title="Deepfake Detection", layout="centered")

st.title("🛡 AI Deepfake Detection System")

uploaded_file = st.file_uploader("Upload Face Image", type=["jpg","png","jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert image to array
    img = np.array(image.resize((128,128)))
    img = img / 255.0
    img = np.reshape(img, (1,128,128,3))

    # Simulated prediction
    prediction = np.random.rand()

    if prediction > 0.5:
        st.error(f"🔴 FAKE ({prediction*100:.2f}%)")
    else:
        st.success(f"🟢 REAL ({(1-prediction)*100:.2f}%)")
