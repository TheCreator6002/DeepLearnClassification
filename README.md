### Functional description of telegram bot
<hr>
<li> Recognition of objects in the image using the Keras framework
<li> Face recognition with a trained model and  Dlib library

##### Classification NN description
<li> Data preparation for neural network training
<li> Training neural network

+ Convolution layer 1
```
model.add(Conv2D(32, (3, 3), input_shape=input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
```

+ Convolution layer 2
```
model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
```

+ Convolution layer 3
```
model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
```

+ Classification layers
```
model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))
```

+ Saved models
```
callbacks = [ModelCheckpoint('Saved_models/Convolution2D.hdf5', 
                              monitor='val_loss', 
                              save_best_only=True)]
```

<li> Using a trained neural network to classify images

##### Verification NN description

<li> Image recognition

+ Descriptor сalculation
```
def descriptor_finding(img):
    sp = dlib.shape_predictor('Saved_models/shape_predictor_68_face_landmarks.dat')
    facerec = dlib.face_recognition_model_v1('Saved_models/dlib_face_recognition_resnet_model_v1.dat')
    detector = dlib.get_frontal_face_detector()
```

+ Euclidean distance calculation
```
def euclidean_distance(function, img1, img2):
    a = distance.euclidean(function(img1), function(img2))
    return a
```

##### Telegram bot

<li> To answer the bot uses the following functions described above

+ Classification
```
answer = answer_bot(file)
```

![Demo classification block](Demo/Test1.gif)

+ Verification
```
answer = euclidean_distance(descriptor_finding, img1, img2 )
```

![Demo verification block](Demo/Test2.gif)
