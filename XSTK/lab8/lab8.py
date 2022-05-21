import pandas as pd
import numpy as np

		#create a sample DataFrame
df = pd.DataFrame({'number': [1,2,3], 'color' : ['red', 'blue', 'white']})

df1 = pd.DataFrame({'number': [1,2,3], 'colors' : ['red', 'blue', 'white']}, columns = ['number' , 'colors'])
#print(df)
#print(df1)

		#create a sample DataFrame using numpy

df2 =pd.DataFrame(np.random.randn(5,3), columns = ['N1', 'N2', 'N3'])
#print(df2)

		#create a DataFrame from dictionary of lists
	
df3 =pd.DataFrame({'N1' :[1,2,3,4] , 'N2' :[4,3,2,1] })
print(df3)

		#create a DataFrame from a list of dictionaries

L = [{'Name' : 'John', 'Last Name' : 'Smith' },{'Name' :  'Mary', 'Last Name' : 'Wood'}]
df4 = pd.DataFrame(L)
#print(df4)

		#input from text Files
	#load data from file
data = pd.read_csv("sample.txt", delimiter = ',')
#print(data)

	#access data
df5 = pd.DataFrame(np.random.randn(10,3), columns = ['N1', 'N2', 'N3'])
#print(df5)


#exercise
import math

#ex1
data1 = pd.read_csv("iris.csv", delimiter = ',')
#print(data1)

count_sepal_length = len(data1['sepal_length'])
count_sepal_width = len(data1['sepal_width'])
count_petal_length = len(data1['petal_length'])
count_petal_width = len(data1['petal_width'])

def sepal_length():
    temp = 0
    for i in range(0,150):
        temp += data1['sepal_length'][i]
    return temp / 150.0

def sepal_width():
    temp = 0
    for i in range(0,150):
        temp += data1['sepal_width'][i]
    return temp / 150
    
def petal_length():
    temp = 0
    for i in range(0,150):
        temp += data1['petal_length'][i]
    return temp / 150

def petal_width():
    temp = 0
    for i in range(0,150):
        temp += data1['petal_width'][i]
    return temp / 150

def variance(data, ddof=0):
    n = len(data)
    mean = sum(data) / n
    return sum((x - mean) ** 2 for x in data) / (n - ddof)

def stdev(data):
    var = variance(data)
    std_dev = math.sqrt(var)
    return std_dev


info = data1.describe()
data2 = pd.DataFrame({'Sepal_length': [count_sepal_length, sepal_length(), 0, 0, 0], 
                       'Sepal_width': [count_sepal_width, sepal_width(), 0, 0, 0],
                       'Petal_length': [count_petal_length, petal_length(), 0, 0, 0], 
                       'Petal_width': [count_petal_width, petal_width(), 0, 0, 0]}, 
                        index= ['count','mean','std','min','max'])
print(data2)


#ex2
dataEX2 = pd.read_csv("population.csv", delimiter = ',')
#print(dataEX2)









