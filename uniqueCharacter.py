#Task-5-Question-4-Take a string and return unique character

def uniqueChar(name):
    dups = []
    noDups = []
    uChar =[]
   
    # Find duplicate and no Duplicate
    for j in name:
        if (j not in noDups):
            noDups.append(j)
        else:
            dups.append(j)
    #print(dups)
    #print(noDups)

    # Compare duplicate and name and remove duplicates and find the number of unique character
    for k in name:
        if ( k not in dups):
            uChar.append(k)
    print("The unique character: ", uChar)
    print("The number of unique Characters: ", len(uChar))

name = input("Please enter name: ")
uniqueChar(name)