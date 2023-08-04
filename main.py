import os
import time
import webbrowser
def main():
    t = 0
    while t < 5:
        os.system('clear')
        os.system('figlet Secret 1.0')
        print("--------------------")
        print("file:")
        os.system('tree')
        print("--------------------")
        scelta_utente = input("enter file name to remove (with exstetion): ")
        os.system(f'rm {scelta_utente}')
        time.sleep(2)
        scelta = input("\nenter the choice: (y/n) --> ")
        if scelta == "y":
            t+=1
        else:
            break
main()
