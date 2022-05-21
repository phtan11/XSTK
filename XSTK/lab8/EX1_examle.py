import math
import pandas as pd
DATA = pd.read_csv("iris.csv", delimiter = ',')
# print(DATA)
# print(DATA.head(5))

count_sepal_length = len(DATA['sepal_length'])
count_sepal_width = len(DATA['sepal_width'])
count_petal_length = len(DATA['petal_length'])
count_petal_width = len(DATA['petal_width'])

def mean_sepal_length():
    temp = 0
    for i in range(0,150):
        temp += DATA['sepal_length'][i]
    return temp / 150.0

def mean_sepal_width():
    temp = 0
    for i in range(0,150):
        temp += DATA['sepal_width'][i]
    return temp / 150
    
def mean_petal_length():
    temp = 0
    for i in range(0,150):
        temp += DATA['petal_length'][i]
    return temp / 150

def mean_petal_width():
    temp = 0
    for i in range(0,150):
        temp += DATA['petal_width'][i]
    return temp / 150

def variance(data, ddof=0):
    n = len(data)
    mean = sum(data) / n
    return sum((x - mean) ** 2 for x in data) / (n - ddof)

def stdev(data):
    var = variance(data)
    std_dev = math.sqrt(var)
    return std_dev


info = DATA.describe()
DATA_1 = pd.DataFrame({'Sepal_length': [count_sepal_length, mean_sepal_length(), 0, 0, 0], 
                       'Sepal_width': [count_sepal_width, mean_sepal_width(), 0, 0, 0],
                       'Petal_length': [count_petal_length, mean_petal_length(), 0, 0, 0], 
                       'Petal_width': [count_petal_width, mean_petal_width(), 0, 0, 0]}, 
                        index= ['count','mean','std','min','max'])
print(DATA_1)