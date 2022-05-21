import random
from collections import Counter
alpha ="abcdefghijklmnopqrstuvwxyz"
l = list(alpha)
random.shuffle(l)
key = ''.join(l)


#encryption
def encryption(plaintext,key):
    alphabet ="abcdefghijklmnopqrstuvwxyz " 
    NewPlaintext = "" 
    newKey = "" 
    for c in plaintext:
        if c in alphabet:
            NewPlaintext += c 
    for c in key:
        if c in alphabet:
            if c != " ":
                if c not in newKey:
                    newKey = newKey + c 
    for c in alphabet:
        if c not in newKey:
            newKey = newKey + c 
    
    indexOfPlainText = []  
    for c in NewPlaintext:
        indexOfPlainText.append(alphabet.index(c)) 

    Ciphertext = ""
    characters= "" 
    for idx in indexOfPlainText:
        characters += newKey[idx] 

        Ciphertext += characters 
        
        characters= ""
    return Ciphertext 


def decryption(ciphertext):
    storedLetter = {} #dictionary
    for c in ciphertext:
        if c not in storedLetter:
            storedLetter[c] = 1
        else:
            storedLetter[c] += 1

    #sort letter turn into array
    cipherSorted = Counter(storedLetter).most_common()

    j =0
    for i in cipherSorted:
        if i[0] == ' ':
            continue
        else:
            ciphertext = ciphertext.replace(i[0],charactersUutien[j])
            j = j+1
            
    decrypted_plaintext=ciphertext

    return(decrypted_plaintext)



#test

charactersUutien = ['e','t','a','o','i','n','s','h','r','d','l','c','u', #kí tự ưu tiên được thay thế
                    'm','w','f','g','y','p','b','v','k','j','x','q','z']
                    

plaintext ="A long time ago, in a galaxy far, far away... It is a dark time for the Rebellion. Although the Death Star has been destroyed, Imperial troops have driven the Rebel forces from their hidden base and pursued them across the galaxy. Evading the dreaded Imperial Starfleet, a group of freedom fighters led by Luke Skywalker has established a new secret base on the remote ice world of Hoth. The evil lord Darth Vader, obsessed with finding young Skywalker, has dispatched thousands of remote probes into the far reaches of space"
plaintext = plaintext.lower()
print(key)
print(plaintext)


print("\nsau khi mã hóa:")
ciphertext = encryption(plaintext, key)
print(ciphertext)

print("\nsau khi giải mã:")
print(decryption(ciphertext))