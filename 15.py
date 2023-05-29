import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM

path = 'c:/_data/'

chinese = pd.read_csv(path + 'chinese.csv', index_col=0, encoding='cp949')
print(chinese.info)