from keras_preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.callbacks import ModelCheckpoint

# Training dataset directory
train_dir = 'Data/train'
# Val dataset directory
val_dir = 'Data/val'
# Test dataset directory
test_dir = 'Data/test'

# Size images
img_width, img_height = 150, 150
# Size input tensor
input_shape = (img_width, img_height, 3)
# epochs quantity
epochs = 30
# batch size
batch_size = 20
# quantity images for train
numbers_train_samples = 17500
# quantity images for validation
numbers_validation_samples = 3750
# quantity images for test
numbers_test_samples = 3750

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

# compiling NN
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# saved models
callbacks = [ModelCheckpoint('Saved_models/Convolution2D.hdf5', monitor='val_loss', save_best_only=True)]

# image generator
datagen = ImageDataGenerator(rescale=1. / 255)

# image generator train dataset
train_generator = datagen.flow_from_directory(train_dir,
                                              target_size=(img_width, img_height),
                                              batch_size=batch_size,
                                              class_mode='binary')

# image generator validation dataset
val_generator = datagen.flow_from_directory(val_dir,
                                            target_size=(img_width, img_height),
                                            batch_size=batch_size,
                                            class_mode='binary')

# image generator test dataset
test_generator = datagen.flow_from_directory(test_dir, target_size=(img_width, img_height),
                                             batch_size=batch_size,
                                             class_mode='binary')

# train model with image generator
model.fit_generator(train_generator,
                    steps_per_epoch=numbers_train_samples // batch_size,
                    epochs=epochs,
                    validation_data=val_generator,
                    validation_steps=numbers_validation_samples // batch_size,
                    callbacks=callbacks)


