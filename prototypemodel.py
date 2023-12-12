import numpy as np

import tensorflow as tf

from tensorflow import keras
import positions


from keras import datasets, layers, models


import random


inp = tf.keras.Input(shape =(8, 8,15) )
l1 = layers.Conv2D(20, (3, 3), padding="same", activation='relu')(inp)
l2 = layers.Conv2D(20, (3, 3), padding="same", activation='relu')(l1)
l3 = layers.Conv2D(20, (3, 3), padding="same", activation='relu')(l2)
l4 = layers.Conv2D(20, (3, 3), padding="same", activation='relu')(l3)
l5 = layers.Conv2D(20, (3, 3), padding="same", activation='relu')(l4)
l6 = layers.Conv2D(20, (3, 3), padding="same", activation='relu')(l5)
l7 = layers.Conv2D(20, (3, 3), padding="same", activation='relu')(l6)
l8 = layers.Conv2D(20, (3, 3), padding="same", activation='relu')(l7)
l9 = layers.Conv2D(20, (3, 3), padding="same", activation='relu')(l8)
l10 = layers.Conv2D(20, (3, 3), padding="same", activation='relu')(l9)
l11 = layers.Conv2D(20, (3, 3), padding="same", activation='relu')(l10)
l12 = layers.Conv2D(20, (3, 3), padding="same", activation='relu')(l11)
l13 = layers.Conv2D(20, (3, 3), padding="same", activation='relu')(l12)
l14 = layers.Conv2D(20, (3, 3), padding="same", activation='relu')(l13)
l15 = layers.Conv2D(20, (3, 3), padding="same", activation='relu')(l14)


l16 = layers.Flatten()(l15)

"""l17 = layers.Dense(4096, activation = 'relu')(l16)
l18 = layers.Dense(4096, activation = 'relu')(l17)
l19 = layers.Dense(4096, activation = 'relu')(l18)
l20 = layers.Dense(4096, activation = 'relu')(l19)"""

policyOut = layers.Dense(4096 , name = "policyHead" , activation = "softmax") ( l16 )
valueOut = layers.Dense (1 , activation = "tanh", name = "valueHead") ( l16)
bce = tf . keras . losses . CategoricalCrossentropy ( from_logits = False )
model = tf.keras.Model( inp , [ policyOut , valueOut ])

model.compile ( optimizer = "SGD",
 loss ={ "valueHead" : "mean_squared_error",
 "policyHead" : bce })

print(model.summary())


#model.fit(x, {"policyHead" : y, "valueHead" : z}, batch_size = 50, epochs = 10)
model.save("v3.keras")


