import numpy as np
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

import pathlib

post_aug_model = tf.keras.models.load_model("./saved_model/post_augmentation")
class_names = ["daisy", "dandelion", "roses", "sunflowers", "tulips"]

sunflower_path = pathlib.Path("./592px-Red_sunflower.jpg")
img_height = 180
img_width = 180

img = keras.preprocessing.image.load_img(
    sunflower_path, target_size=(img_height, img_width)
)
img_array = keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, axis=0)  # Create a batch

prediction = post_aug_model(img_array, training=False)
score = tf.nn.softmax(prediction)

print(
    "This image most likely belongs to {} with a {:.2f} percent confidence.".format(
        class_names[np.argmax(score)], 100 * np.max(score)
    )
)