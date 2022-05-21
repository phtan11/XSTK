import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#line chart
samples = [0.895, 0.91, 0.919,0.926,0.929,0.931]
# plt.plot(samples)


year =[2010, 2011,2012, 2013,2014,2015]
#plt.plot(year,samples)

#add label to the axes

plt.xlabel('Year')
plt.ylabel('yield')
#plt.plot(year,samples)

            #ex1
print("Ex1.a")
iris = pd.read_csv("/iris.csv")
iris.plot (kind="scatter", x='sepal_length', y='sepal_width')
plt.show()

print("Ex1.b")
plt.figure(figsize = (15, 5))
x = iris["sepal_length"]
plt.hist(x, bins=20, color="green")
plt.title("sepal lenght")
plt.xlabel("sepal_lenght")
plt.ylabel("count")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv("/company-sales_data.csv")
# # print(sales)
print("Ex2.a")
profitList = sales['total_profit'].tolist()
monthList = sales['month_number'].tolist()
# # print(profitList)
# # print(monthList)

plt.plot(profitList, monthList)
plt.xlabel('Profit')
plt.ylabel('Month')
plt.title("Profit per month")
plt.show()

print("Ex2.b")
toothpasteSales = sales['toothpaste'].tolist()
# print(toothpasteSales)
plt.scatter(monthList, toothpasteSales)
plt.xlabel('Month')
plt.ylabel('units')
plt.title('Tooth paste Sales per month')
plt.grid(True, linewidth=1, linestyle="--")
plt.show()


print("Ex2.c")
faceCream = sales['facecream'].tolist()
faceWash = sales['facewash'].tolist()

plt.bar([a-0.25 for a in monthList], faceCream, width= 0.25, label = 'Face Cream sales data', align='edge')
plt.bar([a+0.25 for a in monthList], faceWash, width= -0.25, label = 'Face Wash sales data', align='edge')
plt.xlabel('Month')
plt.ylabel('Sales units')
plt.legend(loc='upper left')
plt.title(' Sales data')

plt.grid(True, linewidth= 1, linestyle="--")
plt.title('Facewash and facecream sales data')
plt.show()


#ex3
wordstring = 'it was the best of times it was the worst of times it was the age of wisdom it was the age of foolishness it was the age of wisdom it was the age of foolishness These words are usually the most common in any English language text, so they do not tell us much that is distinctive about Bowsey is trial. In general, we are more interested in finding the words that will help us differentiate this text from texts that are about different subjects. So we are going to filter out the common function words. Words that are ignored like this are known as stop words. We are going to use the following list, adapted from one posted online To keep track of frequencies, we are going to use another type of Python object, a dictionary. The dictionary is an unordered collection of objects. That means that you cannot use an index to retrieve elements from it Dictionaries might be a bit confusing to a new programmer. Try to think of it like a language dictionary.Your list is now clean enough that you can begin analyzing its contents in meaningful ways. Counting the frequency of specific words in the list can provide illustrative data. Python has an easy way to count frequencies, but it requires the use of a new type of variable: the dictionary. Before you begin working with a dictionary, consider the processes used to calculate frequencies in a list. Here, we start with a string and split it into a list, as we’ve done before. We then create an (initially empty) list called wordfreq, go through each word in the wordlist, and count the number of times that word appears in the whole list. '

wordlist = wordstring.split()

wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))

print("String\n" + wordstring +"\n")
print("List\n" + str(wordlist) + "\n")
print("Frequencies\n" + str(wordfreq) + "\n")
print("Pairs\n" + str(list(zip(wordlist, wordfreq))))
