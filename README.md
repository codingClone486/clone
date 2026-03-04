VisionaryAI 🔍

VisionaryAI is an AI-powered image classification web application that predicts objects in uploaded images using a deep learning model. The application is built with TensorFlow/Keras MobileNetV2 and deployed through Streamlit with a modern interactive interface.

Users can upload an image and instantly receive the predicted object label along with confidence percentage.

🚀 Features

- Image upload support (JPG, JPEG, PNG)
- Real-time image classification
- Top prediction with confidence percentage
- Clean dark themed UI
- Built-in user feedback system
- Fast inference using MobileNetV2 pretrained on ImageNet
- Interactive Streamlit interface

🛠️ Tech Stack

- Python
- TensorFlow / Keras
- MobileNetV2
- Streamlit
- NumPy
- PIL (Python Imaging Library)

📷 How It Works

1. User uploads an image.
2. The image is resized to 224 × 224 pixels.
3. Image preprocessing is applied using MobileNetV2 preprocessing.
4. The trained model predicts the object class.
5. The prediction label and confidence score are displayed.

⚙️ Installation

Clone the repository:

https://github.com/codingclone486/visionaryai.git

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

📸 Application Preview

Upload any image and VisionaryAI will identify the object inside the image.

Example predictions:

- Dog 🐶
- Cat 🐱
- Laptop 💻
- Car 🚗
- Food 🍕

📊 Example Output

Prediction example:

Golden Retriever (98.72%)

👨‍💻 Author

Developed by codingclone486

Passionate about building AI-powered applications and machine learning projects.

⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
