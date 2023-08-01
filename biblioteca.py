import os
import time
os.system('clear')
os.system('figlet Biblioteca 1.0')
def main():
    libri = ["Il mondo sfavillante","iaggio al centro della terra","la guerra dei mondi","cicciogamer"]
    request = input("buongiorno,cosa vuole fare vendere o acquistare? (V/A)----> ")
    time.sleep(1.5)

    # scelta vendere
    if request == "v":
        libro = input("enter the book from sell ----> ")
        if libro != libri:
            prezzo = int(input("enter the prive to sell ---> "))
        else:
            print("no riprova")
    # ins libro mancante nella variabile libri nella riga 6
    libri.append(libro)
    print(libri)
main()

