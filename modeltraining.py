
import numpy as np
import positions
import tensorflow as tf
from tensorflow import keras
from keras import datasets, layers, models
import random



x, y, z = positions.a(1000)

model = keras.models.load_model("v3.keras")

print(model.summary())

model.fit(x, {"policyHead" : y, "valueHead" : z}, batch_size = 10, epochs = 10)


model.save("v3.keras")