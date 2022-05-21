import matplotlib.pyplot as plt
import math

def pmf_bernoulli(p, x):
	if x==1:
		return p
	else:
		return 1-p 

def plot_pmf_bernoulli(p):
	X = [0, 1]
	P_bernoulli = [pmf_bernoulli(p,x) for x in X]
	plt.plot(X,P_bernoulli,'o')
	
	plt.title('PMF of Bernoulli p=%.2f' % (p))
	plt.xlabel('Value')
	plt.ylabel('Probability')
	plt.show()
	
#plot_pmf_bernoulli(0.5)

def pmf_binom(k, n, p):
	return math.factorial(n)/(math.factorial(int(k))*math.factorial(n-k)) * pow(p,k) * pow((1-p),(n-k))

def plot_pmf_binom(n, p):
	#K = list(range(0, n+1))
	K = list(range(0,5))
	P_binom = [pmf_binom(k,n,p) for k in K]
	plt.plot(K, P_binom, '-o')
	axes = plt.gca()
	axes.set_xlim([0,n])
	axes.set_ylim([0,1.1*max(P_binom)])
	plt.title('PMF of Binom(%i, %.2f' % (n,p))
	plt.xlabel('Number of k success')
	plt.ylabel('Probability of k success')
	plt.show()
	
#plot_pmf_binom(15,0.5)

def pmf_poisson(k, lam):
	return (pow(lam,k) * pow(math.e,-lam)) / math.factorial(k)
	
def plot_pmf_poisson(n, lam):
	#K = list(range(0,n+1))
	K = list(range(1,5))
	P_poisson = [pmf_poisson(k, lam) for k in K]
	plt.plot(K, P_poisson, '-o')
	plt.title('PMF of Poisson(%i' % (lam))
	plt.xlabel('Number of Events')
	plt.ylabel('Probability of Number of Events')
	plt.show()
	
#plot_pmf_poisson(25,5)
	
def pmf_geo(p,x):
	return p * pow(1-p,x-1)

def plot_pmf_geo(p,n):
	K = list(range(0,n+1))
	P_geo = [pmf_geo(p, k) for k in K]
	plt.plot(K, P_geo, '-o')
	plt.title('PMF of Poisson(%.2f' % (p))
	plt.xlabel('x')
	plt.ylabel('Probability')
	plt.show()

#plot_pmf_geo(0.3,10)

#Ex1
print(pmf_binom(2,5,0.1))
plot_pmf_binom(5,0.1)

#Ex2
print(pmf_poisson(2,3))
plot_pmf_poisson(2,3)

#Ex3
print(pmf_geo(0.4,3))
plot_pmf_geo(0.4,3)