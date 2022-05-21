# from fractions import Fraction
#problem1
S = {'BB','BG','GB','GG'}
B = {s for s in S if 'B' in s} #1 trong 2 la boy
A_B = {s for s in S if s.count('B') == 2} #ca 2 deu la Boy( use SET)
P_A_B = len(A_B)/len(S)
P_B = len(B)/len(S)
# print(B)
# print(A_B)
# print(P_A_B/P_B)

#problem2 (chon ten thanh la female trong 17 student)
P_A = 3/17 #3 hoc sinh ten la "thanh" trong tong 17 student
P_B = 10/17 # 10 female trong 17 student
P_A_B = 1/17 # 1 thanh female trong 17 student

len_P_A_B = (1/17)/(10/17)
# print(len_P_A_B)


#ex1
#a
S = {'MMM','MMF','MFM','FMM','FFM','FMF','MFF','FFF'}
#b
s = len(S)
#c
B = {s for s in S if 'F' in s} 
len_B = len(B)
#d
A = {s for s in S if s.count('F')==3}
len_A = len(A)
#e
result = len_A/len_B #under condition at least one female
print("ex1: %f" %(result))


#ex2
S = [('Thanh', 'Nữ'), ('Hồng', 'Nữ'), ('Thương', 'Nữ'),
 ('Đào', 'Nữ'), ('My', 'Nữ'), ('Yến', 'Nữ'), ('Hạnh', 'Nữ'),
('My', 'Nữ'), ('Vy', 'Nữ'), ('Tiên', 'Nữ'), ('Thanh', 'Nam'),
('Bình', 'Nam'), ('Nhật', 'Nam')
, ('Hào', 'Nam'), ('Đạt', 'Nam'), ('Minh', 'Nam'), ('Thanh', 'Nam')]
#a
A = [] #student co ten la thanh
for s in S:
    if s.count('Thanh')==1:
        A.append(s)
#b
B = [] #student nu
for s in S:
    if 'Nữ' in s:
        B.append(s)
#c
A_B = {s for s in S if (s.count('Thanh') == 1 and 'Nữ' in s)}

#d
P_A = len(A)/len(S)
P_B = len(B)/len(S)
P_A_B = len(A_B)/len(S)
#e
result = P_A_B/P_B #co ten la thanh-female under condition female
print("ex2: %.1f" %(result))


#ex3
import itertools
import random
from itertools import product
# Define ranks , suits and cards
Bai = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'}
Loai = {'Co', 'Ro', 'Chuong', 'Bich'}

#a
Cards = list(product(Bai , Loai))
# print(Cards)

#b
B=list(itertools.combinations(Cards,3)) # 3 cards random
# print(B)

#c
A1= [] #liet ke tat ca truong hop gom 1 hoac 2 con K
for p in B:
    Q = p[0][0] + p[1][0]+p[2][0]
    if Q.count('K') ==1 or Q.count('K') ==2:
        A1.append(p)
# print(A1)

#d
A2=[] # liet ke tat ca cac ptu co it nhat 1 con K
for p in B:
    Q = p[0][0] + p[1][0]+p[2][0]
    if Q.count('K') >=1:
        A2.append(p)
# print(A2)

#e
P_A1 = len(A1)/len(B)
P_A2 = len(A2)/len(B)
print("ex3: P(A1) = %.4f" %(P_A1))
print("     P(A2) = %.4f" %(P_A2))
