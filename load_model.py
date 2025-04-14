import tensorflow as tf

# Load your .h5 model
model = tf.keras.models.load_model(r"C:\Users\shivang\OneDrive\Documents\cat_dog_classifier_fixed\model\cat_dog_model.h5")

# Verify by printing the model summary
model.summary()
