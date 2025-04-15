import streamlit as st
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import decode_predictions, preprocess_input
from PIL import Image
import numpy as np
import time

# Set page config
st.set_page_config(page_title='VisionaryAI', layout='centered')

# Add updated custom CSS for styling with locked black background and footer
st.markdown("""
    <style>
        body {
            font-family: 'Helvetica', sans-serif;
            background-color: #000000 !important; /* Locked black background */
            color: #ffffff !important; /* White text for contrast */
            margin: 0;
            padding: 0;
        }
        .stApp {
            background-color: #000000 !important; /* Ensure the whole app matches background */
        }
        .title {
            text-align: center;
            font-size: 3em;
            color: #00bfff;
            padding-top: 50px;
            font-weight: bold;
            text-shadow: 2px 2px 5px #000000;
        }
        .description {
            font-size: 1.2em;
            color: #f0f0f0;
            text-align: center;
            margin: 20px auto;
            padding: 20px;
            background: rgba(0, 0, 0, 0.6);
            border-radius: 15px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
            max-width: 800px;
            font-weight: 500;
        }
        .upload-box {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            margin-top: 40px;
        }
        .result {
            font-size: 2.5em;
            text-align: center;
            color: #ff6347;
            margin-top: 20px;
            font-weight: bold;
            text-shadow: 2px 2px 5px #000000;
        }
        .feedback-container {
            background: rgba(0, 0, 0, 0.6);
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
            padding: 20px;
            max-width: 600px;
            margin: 20px auto;
            font-size: 1.1em;
        }
        .feedback-container label {
            font-size: 1.1em;
            color: #f0f0f0;
            margin-bottom: 10px;
            display: block;
            text-align: center;
        }
        .footer {
            width: 100%;
            background-color: #000000 !important; /* Locked black footer background */
            color: #dcdcdc; /* Sleek light gray text */
            text-align: center;
            padding: 10px 0;
            border-top: 1px solid #00bfff; /* Slim border for a sleek look */
            font-size: 0.9em; /* Slightly smaller text for a minimalist feel */
        }
        .footer .credits {
            margin: 0;
            font-style: italic; /* Adds a subtle sleekness */
        }
    </style>
""", unsafe_allow_html=True)

# Title of the app
st.markdown('<div class="title">VisionaryAI 🔍</div>', unsafe_allow_html=True)

# Description section
st.markdown("""
    <div class="description">
        Upload an image and let <strong>VisionaryAI</strong> predict what's in it built by <strong>TensorflowV2</strong> and <strong>Keras!</strong>! 📷🧠
    </div>
""", unsafe_allow_html=True)

# File uploader
st.markdown('<div class="upload-box">', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload an image 📸", type=["jpg", "jpeg", "png"])
st.markdown('</div>', unsafe_allow_html=True)

# Load MobileNetV2 model
model = MobileNetV2(weights='imagenet')

# Preprocessing function
def preprocess(img):
    img = img.resize((224, 224))
    img_array = np.array(img)
    if img_array.shape[-1] == 4:
        img_array = img_array[..., :3]  # drop alpha if present
    img_array = np.expand_dims(img_array, axis=0)
    return preprocess_input(img_array)

# Handle uploaded image and prediction
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_container_width=True)

    if st.button("Predict 🧠"):
        with st.spinner("⏳🔄🤔 Processing..."):
            time.sleep(1)  # Simulate processing delay
            try:
                processed_image = preprocess(image)
                preds = model.predict(processed_image)
                decoded = decode_predictions(preds, top=1)[0][0]
                label = f"{decoded[1]} ({decoded[2]*100:.2f}%)"
                st.markdown(f"<div class='result'>{label}</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

    # Feedback Section
    st.markdown('<div class="feedback-container">', unsafe_allow_html=True)
    feedback = st.radio(
        "How satisfied are you with the prediction? 🤔", 
        ["Very satisfied 😊", "Somewhat satisfied 🤨", "Not satisfied 😕"]
    )
    if feedback == "Very satisfied 😊":
        st.write("Fantastic! 🎉 Thank you for using VisionaryAI!")
    elif feedback == "Somewhat satisfied 🤨":
        st.write("Thanks for your feedback! We're always improving! 🚀")
    elif feedback == "Not satisfied 😕":
        st.write("We appreciate your input! Stay tuned for updates! 🛠️")
    st.markdown('</div>', unsafe_allow_html=True)

# Sleek footer
st.markdown("""
    <div class="footer">
        <p class="credits">All rights reserved | Powered by VisionaryAI | Designed and crafted by codingclone486</p>
    </div>
""", unsafe_allow_html=True)
