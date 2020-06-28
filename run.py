import os
import pandas as pd
import glob
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential, save_model, load_model
import matplotlib.pyplot as plt
import numpy as np

def analysis():

  filepath = './saved_model'
  model = load_model(filepath, compile = True)

  one_file = pd.read_csv('presses.csv')
  one_file.columns = ['key','press', 'duration', 'release']
  def df_to_dataset(dataframe, shuffle=True, batch_size=32):
    dataframe = dataframe.copy()
    labels = [0]* dataframe.shape[0]
    ds = tf.data.Dataset.from_tensor_slices((dict(dataframe), labels))
    if shuffle:
      ds = ds.shuffle(buffer_size=len(dataframe))
    ds = ds.batch(batch_size)
    return ds
  batch_size = 10
  run_ds = df_to_dataset(one_file, batch_size=batch_size)

  predictions = model.predict(run_ds)
  print(predictions)
  classes = np.argmax(predictions, axis = 1)
  print(classes)
  sum = 0
  for i in classes:
      sum = sum + i
  avg = sum/len(classes)
  if avg >= .5:
    return True
  else:
    return False
