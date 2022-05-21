import math 

#c2
def pmf_normal(x, mu, sigma):
    """
    Return the probability density function of a normal distribution
    with mean mu and standard deviation sigma.
    """
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

def cdf_normal(x, mu, sigma):
    """
    Return the cumulative density function of a normal distribution
    with mean mu and standard deviation sigma.
    """
    return (1 / 2) * (1 + math.erf((x - mu) / (sigma * (2 ** 0.5))))





#c3
import matplotlib.pyplot as plt  

df = pd.read_csv("company-sales_data.csv")
profitList = df ['total_profit'].tolist()
monthList  = df ['month_number'].tolist()
plt.plot(monthList, profitList, label = 'Month-wise Profit data of last year')
plt.xlabel('Month number')
plt.ylabel('Profit in dollar')
plt.xticks(monthList)
plt.title('Company profit per month')
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()

df = pd.read_csv("company-sales_data.csv")
monthList  = df ['month_number'].tolist()
faceCremSalesData   = df ['facecream'].tolist()
faceWashSalesData   = df ['facewash'].tolist()

plt.bar([a-0.25 for a in monthList], faceCremSalesData, width= 0.25, label = 'Face Cream sales data', align='edge')
plt.bar([a+0.25 for a in monthList], faceWashSalesData, width= -0.25, label = 'Face Wash sales data', align='edge')
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.legend(loc='upper left')
plt.title(' Sales data')

plt.xticks(monthList)
plt.grid(True, linewidth= 1, linestyle="--")
plt.title('Facewash and facecream sales data')
plt.show()


#c4
def freq(str):

	str = str.split()		
	str2 = []

	for i in str:			

		if i not in str2:

			str2.append(i)
			
	for i in range(0, len(str2)):

		print('Frequency of', str2[i], 'is :', str.count(str2[i]))	

def main():
	str ='apple mango apple orange orange apple guava mango mango apple mango apple orange orange apple guava mango mango apple mango apple orange orange apple guava mango mango apple mango apple orange orange apple guava mango mango apple mango apple orange orange apple guava mango mango apple mango apple orange orange apple guava mango mango apple mango apple orange orange apple guava mango mango apple mango apple orange orange apple guava mango mango apple mango apple orange orange apple guava mango mango apple mango apple orange orange apple guava mango mango apple mango apple orange orange apple guava mango mango apple mango apple orange orange apple guava mango mango apple mango apple orange orange apple guava mango mango apple mango apple orange orange apple guava mango mango apple mango apple orange orange apple guava mango mango apple mango apple orange orange apple guava mango mango apple mango apple orange orange apple guava mango mango apple mango apple orange orange apple guava mango mango apple mango apple orange orange apple guava mango mango apple mango apple orange orange apple guava mango mango apple mango apple orange orange apple guava mango mango apple mango apple orange orange apple guava mango mango apple mango apple orange orange apple guava mango mango apple mango apple orange orange apple guava mango mango apple mango apple orange orange apple guava mango mango apple mango apple orange orange apple guava mango mango apple mango apple orange orange apple guava mango mango apple mango apple orange orange apple guava mango mango '
	freq(str)					

if __name__=="__main__":
	main()			 
