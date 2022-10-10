from sklearn.model_selection import train_test_split
from asyncore import read
import pandas as pd

df = pd.read_csv(
    'all-data.csv', names=['Label', 'Text'], encoding='ISO-8859-1')
print(df.head())

print(df.isna().sum)

print(df['Label'].value_counts())

################################

(x_train, x_test, y_train, y_test) = train_test_split(x, y, test_size=0.4)
print(type(x_train.shape))
print(y_train.shape())
print(x_test.shape())
print(y_test.shape())
