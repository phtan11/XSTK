import random
print("ex1:")
#a
def caclulate_dice(n):
    c=0
    for i in range(n):
        xs1 = random.randint(1,6)
        xs2 = random.randint(1,6)
        if xs1 == xs2:
            c+=1
    print("a: ")
    print(c/6)
caclulate_dice(10)

#b
def caclulate_dice(n):
    c=0
    for i in range(n):
        xs1 = random.randint(1,6)
        xs2 = random.randint(1,6)
        if not(xs1 == xs2):
            c+=1
    print("b: ")
    print(c/6)
caclulate_dice(10)

#c
def caclulate_dice(n):
    c=0
    chan=[2,4,6]
    for i in range(n):
        xs1 = random.randint(1,6)
        xs2 = random.randint(1,6)
        if xs1 in chan and xs2 in chan:
            c+=1
    print("c: ")
    print(c/6)
caclulate_dice(10)

#d
def caclulate_dice(n):
    c=0
    chan=[2,4,6]
    for i in range(n):
        xs1 = random.randint(1,6)
        xs2 = random.randint(1,6)
        if xs1 not in chan and xs2 not in chan:
            c+=1
    print("d: ")
    print(c/6)
caclulate_dice(10)

#ex2
print("ex2:")
import itertools
def cross(A,B):
	return {a+b for a in A for b in B}
urn  = cross('B','12') | cross('R','123') | cross('W','12345')
def combos(item, n):
	return {' '.join(combo) for combo in itertools.combinations(item,n)}
U3 = combos(urn,3)

#a
c =0
for i in U3:
    if i.count('R') == 3 or i.count('W') == 3 or i.count('B') == 3:
        c +=1
print("a:")
print(c/len(U3))

#b
c =0
for i in U3:
    if i.count('R') == 1 and i.count('W') == 1 and i.count('B') == 1:
        c +=1
print("b:")
print(c/len(U3))

#c
c =0
for i in U3:
    if not(i.count('R')==3) or not(i.count('W')==3) or not(i.count('B')==3):
        if i.count('R') == 2 or i.count('W') == 2 or i.count('B') == 2:
            c +=1
print("c:")
print(c/len(U3))

#d
c =0
for i in U3:
    if i.count('R') == 2 and i.count('W') == 1:
        c +=1
print("d:")
print(c/len(U3))

#e
c =0
for i in U3:
    if i.count('W') == 3:
        c +=1
print("e:")
print(c/len(U3))


#3
print("ex3:")
from itertools import product
# Define ranks , suits and cards
Bai = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'}
Loai = {'Co', 'Ro', 'Chuong', 'Bich'}
Cards = list(product(Bai , Loai))
B=list(itertools.combinations(Cards,4))

#a
# def simulator_poker(n):
#     c = 0
#     for i in range(n):

# print("a:")
# print(simulator_poker(10))