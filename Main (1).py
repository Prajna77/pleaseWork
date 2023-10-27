import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

def __init__():

    fashion_mnist = tf.keras.datasets.fashion_mnist
    (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

    train_images = train_images / 255.0
    test_images = test_images / 255.0

    return class_names, ((train_images, train_labels), (test_images, test_labels))

def main():

    class_names, data = __init__()
    train_data, test_data = tra
    model = get_model(len(class_names[0]))
    model, hist = train_model(model, data)
    test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

if __name__ == "__main__()":
    main()