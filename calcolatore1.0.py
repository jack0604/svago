import os
import time
import random
os.system('clear')
os.system('figlet Calcolatore 1 . 0')
print("----------------------------------")
time.sleep(2)
os.system('clear')
print("\nsei pronto a iniziare?")
time.sleep(2)
os.system('clear')
while True:
    time.sleep(1.5)
    os.system('clear')
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    print(num1)
    print("+")
    print(num2)
    print("=")
    somma = num1 + num2
    ris = int(input("inserisci il risultato --------> "))
    if ris == somma:
        print("Hai indovinato la somma è " + str(somma))
    else:
        print("Hai sbagliato la somma è " + str(somma))
