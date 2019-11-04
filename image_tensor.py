#!/usr/bin/env python3
from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

print("Image Scraper v.0.0.0 - Image Tensor")
print("TensorFlow version {0}".format(tf.__version__))

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
class_names = ['T-shirt/top',
		'Trouser',
		'Pullover',
		'Dress',
		'Coat',
		'Sandal',
		'Shirt',
		'Sneaker',
		'Bag',
		'Ankle boot']
print("train_images.shape: {0}".format(train_images.shape))
print("len(train_labels): {0}".format(len(train_labels)))
print("train_labels: {0}".format(train_labels))
print("test_images.shape: {0}".format(test_images.shape))
print("len(test_labels): {0}".format(len(test_labels)))

plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()

train_images = train_images / 255.0
test_images = test_images / 255.0

plt.figure(figsize = (10, 10))
for i in range(25):
	plt.subplot(5, 5, i + 1)
	plt.xticks([])
	plt.yticks([])
	plt.grid(False)
	plt.imshow(train_images[i], cmap = plt.cm.binary)
	plt.xlabel(class_names[train_labels[i]])
plt.show()
model = keras.Sequential([keras.layers.Flatten(input_shape = (28, 28)),
		keras.layers.Dense(128, activation = 'relu'),
		keras.layers.Dense(10, activation = 'softmax')])
model.compile(optimizer = 'adam',
		loss = 'sparse_categorical_crossentropy',
		metrics = ['accuracy'])
model.fit(train_images, train_labels, epochs = 10)
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose = 2)
print("\nTest accuracy: {0}", test_acc)
