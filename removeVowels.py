# Task - 5 - Question 3 - Take a string and return string with all the vowels removed

def removeVowels(name):
    char = []
    for n in name:
        if (n != "a" and n != "e" and n !="i" and n != "o" and n != "u"):
            newChar = n
            print(newChar)
                                
name = input("Pleas enter name: ")
removeVowels(name)