import streamlit as st
import numpy as np
from PIL import Image
import cv2

st.set_page_config(page_title="Deepfake Detection", layout="centered")

st.title("🛡 AI Deepfake Detection System")
st.write("Capture image from webcam and detect if it is Real or Fake")

# Webcam capture
img_file = st.camera_input("Take a picture")

if img_file is not None:
    # Convert to image
    image = Image.open(img_file)
    st.image(image, caption="Captured Image", use_column_width=True)

    # Preprocess image
    img = np.array(image.resize((128,128)))
    img = img / 255.0
    img = np.reshape(img, (1,128,128,3))

    # Simulated prediction (replace with real model later)
    prediction = np.random.rand()

    if prediction > 0.5:
        st.error(f"🔴 FAKE ({prediction*100:.2f}%)")
    else:
        st.success(f"🟢 REAL ({(1-prediction)*100:.2f}%)")

