import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator

dogs_train = pd.read_csv('labels.csv', names=['id', 'breed'])
dogs_train['id'] = dogs_train['id'].apply(lambda x : x + '.jpg')

print(dogs_train)

generator = ImageDataGenerator(rescale=1./255)

train_generator = generator.flow_from_dataframe(dataframe=dogs_train, directory='./train/',
        x_col='id', y_col='breed', subset='training')


