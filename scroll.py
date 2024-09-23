import random
import time

alp = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

a = []

wor = input("Enter a word: ").lower() 

j = len(wor)
i = 0

while True:

    n = random.randint(0, 26)
    print("\033c", end="")  
    
    for k in a:
        print(k, end="")
    
    if i < j:
        print(alp[n], end="")

    print("_" * (j - i - 1))

    time.sleep(0.1)

    if wor[i] == alp[n]:
        a.append(alp[n])  
        i += 1
        
    if i == j:
        break
