import itertools

#permutations: n!/(n-k)!
E = [1,2,3,4]
k = 3
p = [p for p in itertools.product(E,repeat = k)] #này có trùng 1 1 1
# print(len(p))
# for i in p:
#     print(i)
# print()
# print()
#another example
E ={'a','b', 'c', 'd'}#[1,2,3,4] 
e = list(itertools.permutations(E,3)) #này hog co  1 1 1, [3 số khác nhau]
# print(len(e))
# for i in e:
#     print(i)

#combination  : [n!/(n-k)!k!]
print()
E = {'a','b', 'c', 'd'}
choose_E = list(itertools.combinations(E,3)) #này là 3 kí tự khác nhau hết
# print(len(choose_E))
# for i in choose_E:
#     print(i)

#URN problem
def cross(A,B):
    return {a+b for a in A for b in B}
URN = cross('W','12345678') | cross('B','123456') | cross('R','123456789')
# print(URN)
#a
U6 = list(itertools.combinations(URN, 6))
# print(len(U6))

#b
# for i in U6:
#     print(i)

#c
# for i in U6:
#     if i[0][0] =='R' and i[-1][0] =='R':
#         print(i)


#ex1
E = [0,1,2,3,4,5,6,7,8,9]
p = list(itertools.permutations(E,4))
print(len(p))

#ex2 
A = {1,2,3,4,5}
num_3_digit = list(itertools.combinations(A,3))
print(len(num_3_digit))
print(num_3_digit)


#ex3
URN3 = cross('W','12345678') | cross('B','123456') | cross('R','123456789')
#a
U3 = list(itertools.combinations(URN3,3))
print(len(U3))
#B
for i in U3:
    mau = i[0][0] + i[1][0] + i[-1][0]
    if len(set(mau)) == 3:
        print(i)
#c
for i in U3:
    if i[0][0] == 'W' and i[1][0] == 'R':
        print(i)

#ex4
M = cross('T','1234')
P = cross('L','123')
C = cross('H','12')
L = 'N'
shelf = list(itertools.product(itertools.permutations(M),itertools.permutations(P),itertools.permutations(C),itertools.permutations(L)))
for i in shelf:
    print(i)
#ex5
URN_combi = cross('M','123456') | cross('F', '123456789')
M3W2 = list(itertools.combinations(URN_combi,5))
for i in M3W2:
    countMan = 0
    countWomen = 0
    for j in range(0,5):
        if i[j][0] == 'M':
            countMan += 1
        else:
            countWomen += 1
    if countMan == 3 and countWomen == 2:
        print(i)

#ex6
deck = cross('SCDH',['1','2','3','4','5','6','7','8','9','10','J','Q','K'])
poker_5 = list(itertools.combinations(deck,5))
len_poker_5 = len(poker_5)
print('Ex6.a:', len_poker_5)

three_of_a_kind = []

for p in poker_5:
    S = 0
    C = 0
    D = 0
    H = 0
    for q in p:
        if q[0]=='S':
            S+=1
        if q[0]=='C':
            C+=1
        if q[0]=='D':
            D+=1
        if q[0]=='H':
            H+=1
    if S==3 or C==3 or D==3 or H==3:
        three_of_a_kind.append(p)

len_three_of_a_kind = len(three_of_a_kind)
print('Ex6.b: ',len_three_of_a_kind)