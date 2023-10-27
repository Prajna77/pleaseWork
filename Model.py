import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


def get_model(num_classes=10):
    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(10)
    ])

def train_model(model, data):
    train_images, train_labels = data

    model.compile(optimizer='adam',
                loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=['accuracy'])

    hist = model.fit(train_images, train_labels, epochs=10)
    return model, hist