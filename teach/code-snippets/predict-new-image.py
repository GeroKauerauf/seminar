class_names = ["daisy", "dandelion", "roses", "sunflowers", "tulips"]
prediction = model(img_array, training=False)
score = tf.nn.softmax(prediction)

print(
    "This image most likely belongs to {} with a {:.2f} percent confidence.".format(
        class_names[np.argmax(score)], 100 * np.max(score)
    )
)