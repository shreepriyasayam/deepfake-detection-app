import streamlit as st
import numpy as np
import cv2
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase
import av

st.title("🛡 AI Deepfake Detection System (Live)")

class VideoProcessor(VideoProcessorBase):
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")

        resized = cv2.resize(img, (128,128))
        resized = resized / 255.0

        # Simulated prediction
        prediction = np.random.rand()

        if prediction > 0.5:
            label = "FAKE"
            color = (0,0,255)
        else:
            label = "REAL"
            color = (0,255,0)

        cv2.putText(img, label, (20,50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, color, 3)

        return av.VideoFrame.from_ndarray(img, format="bgr24")

webrtc_streamer(key="deepfake", video_processor_factory=VideoProcessor)

