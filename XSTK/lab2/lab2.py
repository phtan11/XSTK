#1. define function
D= {1,2,3,4,5,6}
even = {2,4,6}
P = len(even)/len(D)
#print(P)

#2. URN Problem
import itertools
def cross(A,B):
	return {a+b for a in A for b in B}
urn  = cross('W','12345678') | cross('B','123456') | cross('R','123456789')

def combos(item, n):
	return {' '.join(combo) for combo in itertools.combinations(item,n)}
U6 = combos(urn,6)
#print(U6)
#2a
count2A = 0
for i in U6:
	if i.count('R') ==6:
		count2A+=1
P2a = count2A/len(U6)
#print(P2a)

#2b
count2B = 0
for i in U6:
	if i.count('B') == 3 and i.count('W') == 2 and i.count('R')==1:
		count2B +=1
P2b = count2B/len(U6)
#print(P2b)

#2c
count2c = 0
for i in U6:
	if i.count('W')==4:
		count2c +=1
P2c = count2c/len(U6)
#print(P2c)


#ex1
import random
print("ex1:")
def simualtor_dical(n):
	count = 0
	chan =[0,2,4,6]
	for i in range(n):
		Conlac1 = random.randint(0,6)
		Conlac2 = random.randint(0,6)
		if Conlac1 in chan and Conlac2 in chan:
			count+=1
	print(count/n)
simualtor_dical(2)

#ex2
print("ex2")
def simualtor_dice2(n):
	count = 0
	chan =[0,2,4,6]
	le = [1,3,5]
	for i in range(n):
		Conlac1 = random.randint(0,6)
		Conlac2 = random.randint(0,6)
		if (Conlac1 in chan and Conlac2 in le) or (Conlac1 in le and Conlac2 in chan):
			count+=1
	print(count/n)
simualtor_dice2(2)

#ex3
print("ex3:")
def simualtor_dice3(n):
	count = 0
	for i in range(n):
		Conlac1 = random.randint(0,6)
		Conlac2 = random.randint(0,6)
		if Conlac1==Conlac2:
			count+=1
	print(count/n)
simualtor_dice3(2)

#ex4
print("Ex4")
def simualtor_dice4(n):
	count = 0
	for i in range(n):
		Conlac1 = random.randint(0,6)
		Conlac2 = random.randint(0,6)
		if (Conlac1== 1 and Conlac2 == 6) or (Conlac1== 6 and Conlac2 == 1):
			count+=1
	print(count/n)
simualtor_dice4(2)

#ex5
print("Ex5")
def simualtor_dice5(n):
	count = 0
	for i in range(n):
		Conlac1 = random.randint(0,6)
		Conlac2 = random.randint(0,6)
		if (Conlac1+Conlac2) > 6:
			count+=1
	print(count/n)
simualtor_dice5(2)

#ex6
import random
from itertools import product
# Define ranks , suits and cards
Ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}
Suits = {'Co', 'Ro', 'Chuong', 'Bich'}
Cards = list(product(Ranks , Suits))

print("ex6:")
def simualtor_poker1(n):
    count = 0
    co = ['Co']
    for i in range(n):
        la1 = random.randint(0,51)
        la2 = random.randint(0,51)
        la3 = random.randint(0,51)
        la4 = random.randint(0,51)
        if Cards[la1][1] in co and Cards[la2][1]in co and Cards[la3][1] in co and Cards[la4][1]in co and Cards[la5][1] in co:
            count+=1
    print(count/n)
simualtor_poker1(100)

#ex7
print("ex7:")
def simualtor_poker2(n):
    count = 0
    stack = ['Co','Ro','Chuong','Bich']
    contain = []
    for i in range(n):
        la1 = random.randint(0,51)
        la2 = random.randint(0,51)
        la3 = random.randint(0,51)
        la4 = random.randint(0,51)
        if Cards[la1][1] in stack:
            contain.append(Cards[la1][1])
            if Cards[la2][1] in stack and not(Cards[la2][1] in contain):
                contain.append(Cards[la2][1])
                if Cards[la3][1] in stack and not(Cards[la3][1] in contain):
                    contain.append(Cards[la3][1])
                    if Cards[la4][1] in stack and not(Cards[la4][1] in contain):
                        count+=1
    print(count/n)
simualtor_poker2(100)

#ex8
print("Ex8")
countEx7 = 0
for i in U6:
    if i.count('W') == 2 and i.count('R') == 2 and i.count('B') == 2:
        countEx7 +=1
print(countEx7/len(U6))