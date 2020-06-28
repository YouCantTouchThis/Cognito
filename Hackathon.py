#Import statements
import numpy as np 
import pandas as pd 
import functools
import os
import matplotlib.pyplot as plt
from itertools import chain
import sklearn.model_selection as skl
from random import sample 
from tensorflow import keras
from tensorflow.keras import layers
from keras.models import Sequential
from keras.layers import Dense, Dropout
import tensorflow as tf
from keras.optimizers import Adam
import csv
from csv import writer
import glob
from sklearn.model_selection import train_test_split
from tensorflow import feature_column
from tensorflow.keras.models import Sequential, save_model, load_model

#Machine Learning Code
#Get the data from folders
groundTruth1_df = pd.read_csv(r'C:/Users/anish_8d0sbo2/Hackathon3/neuroqwerty-mit-csxpd-dataset-1.0.0/data/groundTruths/GT_DataPD_MIT-CS1PD.csv')
groundTruth2_df = pd.read_csv(r'C:/Users/anish_8d0sbo2/Hackathon3/neuroqwerty-mit-csxpd-dataset-1.0.0/data/groundTruths/GT_DataPD_MIT-CS2PD.csv')
#Converting ground truths from second file of groundtruth file 1
#The values of ground truth file 1 had two sets of data for each person
groundTruth3_df = groundTruth1_df.copy()
del groundTruth3_df['file_1']
groundTruth3_df['file_1'] = groundTruth3_df['file_2']
del groundTruth3_df['file_2']
frames = [groundTruth1_df, groundTruth2_df, groundTruth3_df]
all_data = pd.concat(frames)
#Convert ground truth from true false to 1,0
groundTruth1_df['gt'] = groundTruth1_df['gt'].astype(int)
groundTruth2_df['gt'] = groundTruth2_df['gt'].astype(int)
groundTruth3_df['gt'] = groundTruth3_df['gt'].astype(int)
all_data['gt'] = all_data['gt'].astype(int)

#Add data into the ground truth dataframe
#file_len = 3000
#for file in all_data['file_1']:
#    temp_file = pd.read_csv(r'C:/Users/anish_8d0sbo2/Hackathon3/neuroqwerty-mit-csxpd-dataset-1.0.0/data/MIT-CS1PD/'+ file)
#    temp_file = temp_file.iloc[:300]
#    temp_file['class'] = np.full(shape = 300, fill_value = all_data.loc[all_data.file_1 == file, 'gt'].values[0])
#    temp_file.columns = ['key','press', 'duration', 'release', 'class']

#    temp_file.to_csv(r'C:/Users/anish_8d0sbo2/Hackathon3/neuroqwerty-mit-csxpd-dataset-1.0.0/data/MIT-CS1PD/'+ file)

#for file in all_data['file_1']:
#    with open(r'C:/Users/anish_8d0sbo2/Hackathon3/neuroqwerty-mit-csxpd-dataset-1.0.0/data/MIT-CS1PD/'+ file, "a") as fp:
#        wr = csv.writer(fp, dialect='excel')
#        wr.writerow(np.array(['class', all_data.loc[all_data.file_1 == file, 'gt'].values[0], 0 , 0]))
#for file in groundTruth1_df['file_1']:
#    with open(r'C:/Users/anish_8d0sbo2/Hackathon3/neuroqwerty-mit-csxpd-dataset-1.0.0/data/MIT-CS1PD/'+ file, "a") as fp:
#        wr = csv.writer(fp, dialect='excel')
#        wr.writerow(np.array(['class', groundTruth1_df.loc[groundTruth1_df.file_1 == file, 'gt'].values[0]]))

#for file in groundTruth2_df['file_1']:
#    with open(r'C:/Users/anish_8d0sbo2/Hackathon3/neuroqwerty-mit-csxpd-dataset-1.0.0/data/MIT-CS1PD/'+ file, "a") as fp:
#        wr = csv.writer(fp, dialect='excel')
#        wr.writerow(np.array(['class', groundTruth2_df.loc[groundTruth2_df.file_1 == file, 'gt'].values[0]]))

#for file in groundTruth3_df['file_1']:
#    with open(r'C:/Users/anish_8d0sbo2/Hackathon3/neuroqwerty-mit-csxpd-dataset-1.0.0/data/MIT-CS1PD/'+ file, "a") as fp:
#        wr = csv.writer(fp, dialect='excel')
#        wr.writerow(np.array(['class', groundTruth3_df.loc[groundTruth3_df.file_1 == file, 'gt'].values[0]]))


#split data into test & validation sets with 80/20 split
data_files = glob.glob(r'C:/Users/anish_8d0sbo2/Hackathon3/neuroqwerty-mit-csxpd-dataset-1.0.0/data/MIT-CS1PD/*.csv')
dfs = []
for filename in data_files:
    dfs.append(pd.read_csv(filename))
one_file = pd.concat(dfs, ignore_index = True)

print(one_file.sample(2))
print (one_file.dtypes)
print(one_file.sample(10))
one_file['key'] = pd.Categorical(one_file['key'])
one_file['key'] = one_file.key.cat.codes
print (one_file.dtypes)
del one_file['Unnamed: 0']
train, test = train_test_split(one_file, test_size=0.2)
train, val = train_test_split(train, test_size=0.2)
print(len(train), 'train examples')
print(len(val), 'validation examples')
print(len(test), 'test examples')
def df_to_dataset(dataframe, shuffle=True, batch_size=32):
  dataframe = dataframe.copy()
  labels = dataframe.pop('class')
  ds = tf.data.Dataset.from_tensor_slices((dict(dataframe), labels))
  if shuffle:
    ds = ds.shuffle(buffer_size=len(dataframe))
  ds = ds.batch(batch_size)
  return ds


batch_size = 10
train_ds = df_to_dataset(train, batch_size=batch_size)
val_ds = df_to_dataset(val, shuffle=False, batch_size=batch_size)
test_ds = df_to_dataset(test, shuffle=False, batch_size=batch_size)
for feature_batch, label_batch in train_ds.take(1):
  print('Every feature:', list(feature_batch.keys()))
example_batch = next(iter(train_ds))[0]
def demo(feature_column):
  feature_layer = layers.DenseFeatures(feature_column)
  print(feature_layer(example_batch).numpy())
release = feature_column.numeric_column("release")
print(feature_column.numeric_column("release"))
demo(release)

feature_columns = []

print(one_file.columns)
for header in ['press', 'duration', 'release']:
    print(feature_column.numeric_column(header))
    feature_columns.append(feature_column.numeric_column(header))
print(feature_columns)
feature_layer = tf.keras.layers.DenseFeatures(feature_columns)
model = tf.keras.Sequential([
  feature_layer,
  layers.Dense(128, activation='relu'),
  layers.Dense(128, activation='relu'),
  layers.Dense(1)
])


model.compile(optimizer='adam',loss = 'categorical_crossentropy', metrics=['accuracy'])

checkpoint_path = "training_1/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)
cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,save_weights_only=True,verbose=1)
model.fit(train_ds, validation_data = val_ds, epochs = 5, callbacks = [cp_callback] )
filepath = './saved_model'
save_model(model, filepath)

loss, accuracy = model.evaluate(test_ds)
print("Accuracy:", accuracy)

