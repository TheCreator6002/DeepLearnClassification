import matplotlib.pyplot as plt
import tensorflow.keras.preprocessing.image as im
import tensorflow as tf
import numpy as np
import os
from keras_preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.callbacks import ModelCheckpoint

# Size images
img_width, img_height = 150, 150
# Size input tensor
input_shape = (img_width, img_height, 3)

# model NN
model = Sequential()
# convolution layer 1
model.add(Conv2D(32, (3, 3), input_shape=input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

# convolution layer 2
model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

# convolution layer 3
model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

# classification layers
model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))
model.load_weights('Saved_models/Convolution2D.hdf5')

# compiling NN
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

img_size = 150
image_path = 'Data/check/11.jpg'
img = im.load_img(image_path, target_size=(img_size, img_size))
plt.imshow(img)
plt.show()

img = np.expand_dims(img, axis=0)
result = model.predict_classes(img)

if result == [[0]]:
    print("Это собака!")
elif result == [[1]]:
    print("Это кошка!")
else:
    print(result)






