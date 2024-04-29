#from keras.models import load_model  # TensorFlow is required for Keras to work
import keras
import tensorflow as tf
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import os
project_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sub_folder="ImageClassification"
file_name_model="model.savedmodel"
file_name_labels="labels.txt"
file_name_image="prova_reload.jpg"
print("Current folder:", project_folder) #project folder uguale per tutti
file_absolute_path_model = os.path.join(project_folder, sub_folder, file_name_model)
file_absolute_path_labels = os.path.join(project_folder, sub_folder, file_name_labels)
file_absolute_path_image = os.path.join(project_folder, sub_folder, file_name_image)
#file_relative_path = 'keras_model.h5'
#file_relative_path_model = 'model.savedmodel'

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)
# file_absolute_path_model = r'C:\Users\Luca\HRI\hri\ImageClassification\model.savedmodel'
# file_absolute_path_labels = r'C:\Users\Luca\HRI\hri\ImageClassification\labels.txt'
# file_absolute_path_image = r'C:\Users\Luca\HRI\hri\ImageClassification\prova_reload.jpg'
# Load the model
#model = load_model(file_relative_path, compile=False)
model=keras.layers.TFSMLayer(file_absolute_path_model, call_endpoint="serving_default")
# Load the labels
class_names = open(file_absolute_path_labels, "r").readlines()
#class_names = open("labels.txt", "r").readlines()

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Replace this with the path to your image
image = Image.open(file_absolute_path_image).convert("RGB")

# resizing the image to be at least 224x224 and then cropping from the center
size = (224, 224)
image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

# turn the image into a numpy array
image_array = np.asarray(image)

# Normalize the image
normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

# Load the image into the array
data[0] = normalized_image_array

# Predicts the model
prediction = model(data)
prediction=list(prediction.values())[0]
#prediction=prediction['sequential_19']
if isinstance(prediction, tf.Tensor):
    prediction = prediction.numpy()
prediction=prediction[0]
index = np.argmax(prediction)
class_name = class_names[index]
confidence_score = prediction[index]

# # Print prediction and confidence score
print("Class:", class_name[2:], end="")
print("Confidence Score:", confidence_score)