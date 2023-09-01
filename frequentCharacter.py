# Task-5 -Question-7 - Return a most frequent character in a string

def frequentCharacter(name):
    noDups = []
    dups = []

    for i in name:
        if i not in noDups:
            noDups.append(i)
        else:
         dups.append(i)
    #print(noDups)
    #print(dups)   
    
    freqChar = max(set(dups), key = dups.count)
    print("The most frequent character in a enetered string: ",freqChar)

name = input("Please enter a string to find most frequent character in it: ")
frequentCharacter(name)


