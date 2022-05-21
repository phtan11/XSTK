import random
import fractions
#definitions
x= [random.randint(1,6) for i in range(8000)]
# print(x) # ca dong 
X = set(x)
# print(X) # 1 2 3 4 5 6

#probability distribution
P = [x.count(i)/len(x) for i in X] #dem cac so trog x ruif chia cho tong cua x
print("P:")
print(P) 

#Cumulative distribution function – CDF
FX = sum(P[:3])  #tinh tong 4 (gom 0 1 2 3 ) so dau tien cua P
print("FX= %f" %(FX)) 

#5.1 Expectations
#u =E(X) = xich ma cua xi*px
EX  =0 
for x in X:
    EX = EX + (x*P[x-1])
print("EX= %f" %(EX))

#5.2 Variance (phuong Sai)
#Var(X) = xich ma cua (xi - E(X)^2*Pi
import math
VarX = 0
for x in X:
    VarX = VarX + math.pow(x - EX,2)*P[x-1]
print("VarX= %f" %(VarX))

#5.3 Standard Deviation (DO LEch Chuan)
SD = math.sqrt(VarX)
print("SD= %f" %(SD))

#5.4 Standard Score - SC (diem chuan)
z = 0
for x in X:
    z = (x - EX)/SD
print("z= %f" %(z))

#ex1
print("Ex1:")
x = [random.randint(0,5) for i in range(3650)]
#a
print("a:")
X = set(x)
print(X)

#b
print("b:")
P =[x.count(i)/len(x) for i in X]
print(P)

#c
print("c:")

#expectation EX1 = u
EX1 = 0
for x in X:
    EX1 = EX1 + (x*P[x-1])
print("EX of ex1= %f" %(EX1))

#Variance
VarEx1 = 0
for x in X:
    VarEx1 = VarEx1 + math.pow((x-EX1),2)*P[x-1]
print("VarX of ex1= %f" %(VarEx1))

#Standard Deviation
SDEx1 = math.sqrt(VarEx1)
print("SD of ex1= %f" %(SDEx1))

#d
print("d:")
tong = P[0] + P[5] + P[3]
print(tong)

#ex2
x = [random.randint(0,2) for i in range(10000)]
X = set(x)
P = [x.count(i)/len(x) for i in X]
print(P)
EX = 0
for a in X:
    EX = EX + (a*P[a-1])
print(EX)
VarX = 0
for a in X:
    VarX = VarX + (a-EX)*(a-EX)*P[a-1]
print(VarX)
SD = math.sqrt(VarX)
print(SD)
A = 0
for a in x:
    if a>=1:
        A=A+1
print(fractions.Fraction(A,len(x)))