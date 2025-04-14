import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import time

# Set page config
st.set_page_config(page_title='Cat vs Dog Classifier', layout='centered')

# Add custom CSS for styling
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #000000;  /* Black background */
            color: #ffffff;  /* White text color */
            margin: 0;
            padding: 0;
        }

        .title {
            text-align: center;
            font-size: 3em;
            color: #3498db;  /* Blue color */
            padding-top: 50px;
            font-weight: bold;
        }

        .description {
            font-size: 1.2em;
            color: #ecf0f1;  /* Light grey text */
            text-align: center;
            margin-top: 20px;
            padding: 20px;
            background-color: #34495e;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
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
            font-size: 2em;
            text-align: center;
            color: #e74c3c;
            margin-top: 20px;
            font-weight: bold;
        }

        .feedback {
            text-align: center;
            margin-top: 30px;
        }

        .footer {
            position: relative;
            bottom: 0;
            width: 100%;
            background-color: #34495e;
            color: white;
            text-align: center;
            padding: 20px;
            font-size: 1em;
        }

        .footer p {
            font-size: 1.1em;
            margin: 10px 0;
        }

        .footer .credits {
            font-size: 0.9em;
            color: #bdc3c7;
        }

        .footer .credits a {
            color: #e74c3c;
            text-decoration: none;
        }

        .footer .credits a:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# Title of the app
st.markdown('<div class="title">Cat vs Dog Classifier 🐱🐶</div>', unsafe_allow_html=True)

# Shortened Description
st.markdown("""
    <div class="description">
        Upload an image, and our AI-powered model will predict if it's a <strong>Cat 🐱</strong> or a <strong>Dog 🐶</strong>. 
        Built with <strong>TensorFlow</strong> and <strong>Keras</strong>!
    </div>
""", unsafe_allow_html=True)

# File uploader
st.markdown('<div class="upload-box">', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload an image 📸", type=["jpg", "jpeg", "png"])
st.markdown('</div>', unsafe_allow_html=True)

# Load pre-trained model
model = tf.keras.models.load_model("cat_dog_model.h5")

# Preprocessing function
def preprocess(img):
    img = img.resize((160, 160))
    img = np.array(img) / 255.0
    return np.expand_dims(img, axis=0)

# Handle uploaded image and prediction
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_container_width=True)

    # Button to predict after the image is uploaded
    if st.button("Predict 🧠"):
        # Display processing emojis while prediction is happening
        processing_text = "⏳🔄🤔 Processing..."
        with st.spinner(processing_text):
            time.sleep(2)  # Simulate processing time
            try:
                # Check the image preprocessing
                processed_image = preprocess(image)
                
                # Predict and handle result
                pred = model.predict(processed_image)

                if pred is None or len(pred) == 0:
                    st.error("Error: The prediction returned an empty result!")
                else:
                    result = "Dog 🐶" if pred[0][0] > 0.5 else "Cat 🐱"
                    st.markdown(f"<div class='result'>{result}</div>", unsafe_allow_html=True)

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

        # Interesting button to try more with curious emojis
        if st.button("Interesting! Want to try more? 🤔👀"):
            # Show the file uploader again for new image upload
            uploaded_file = st.file_uploader("Upload an image 📸", type=["jpg", "jpeg", "png"])

    # Feedback Section with emojis
    st.markdown('<div class="feedback">', unsafe_allow_html=True)
    feedback = st.radio("Are you satisfied with the prediction? 🤔", ("Yes 👍", "No 👎"))
    if feedback == "Yes 👍":
        st.write("Great! 🎉 We're happy you like it!")
    elif feedback == "No 👎":
        st.write("We are improving! 🛠️ Stay tuned for better predictions!")
    st.markdown('</div>', unsafe_allow_html=True)

# Footer section (updated to no shadow and positioned at the bottom)
st.markdown("""
    <div class="footer">
        <p>Designed and curated by <strong><a href="https://www.instagram.com/codingclone486/" target="_blank">codingclone486</a></strong></p>
        <div class="credits">
            <p>&#169; 2025 All Rights Reserved</p>
        </div>
    </div>
""", unsafe_allow_html=True)
