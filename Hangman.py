from getpass import getpass
import string
word = getpass("Please Enter a Word: ")
tahmin = []
lettersaid = []
for x in word:
    tahmin.append("_")
"""Kelimede her harf icin (_) koyar"""

def print_board(a):
    print (" ".join(a))

"""listeyi stringleri birlestirerek yazdirir"""
print_board(tahmin)


def takeguess(x):
    x = input("Please Enter a Letter: ")
    in_word(x)

""" Harf ister, in_word e sokar"""

def is_valid(guess):
    if guess in string.ascii_letters and len(guess) == 1:
        return True
    else:
        print ("That's not a real letter")
        return False
"""Girilen karakter harf mi degil mi kontrol eder"""

def in_word(letter):
    global count
    global lettersaid
    counter=0
    if is_valid(letter) == True:
        if letter not in lettersaid:
            lettersaid.append(letter)
            if letter in word:
                for q in word:
                    if (letter == q):
                        tahmin[counter] = q
                        counter+=1
                    else:
                        counter+=1
                print_board(tahmin)
            else:
                count = count - 1
        else:
            print ("You guessed that already")
            
"""karakter harf ise daha once soylenmis mi bakar, 
    soylenmemisse soylenmisler arasina ekler ve kelimede var mi bakar,
    kelimedeyse harfi(_) yerine koyar ve yazdirir degilse kalan haklari 1 azaltir"""

count = 10
while count>0:
    takeguess(x)
        
    if "_" in tahmin:
        print ("Guesses left: " + str(count))
    else:    
        print ("YOU WIN!!!")
        break
        
else:
    print ("Game Over!")
