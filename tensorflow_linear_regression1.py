import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from six.moves import urllib
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental import preprocessing

normalize = preprocessing.Normalization()

abalone_train = pd.read_csv(
    "https://storage.googleapis.com/download.tensorflow.org/data/abalone_train.csv",
    header=None,
    names=["Length", "Diameter", "Height", "Whole weight", "Shucked weight",
           "Viscera weight", "Shell weight", "Age"]
)

#print(abalone_train.head())

abalone_features = abalone_train.copy()
abalone_labels = abalone_features.pop('Age')

#print(abalone_features.head())

abalone_features = np.array(abalone_features)
normalize.adapt(abalone_features)

#print(abalone_features)

abalone_model = tf.keras.Sequential([
        layers.Dense(64),
        layers.Dense(1)
    ])

abalone_model.compile(loss= tf.losses.MeanSquaredError(),
                        optimizer= tf.optimizers.Adam())

abalone_model.fit(abalone_features, abalone_labels, epochs=100)