#Task-5 -Question-9 Find number of words in the string

def numOfWord(name):
    names =[]
    count =1
    for i in name:
        names.append(i)
    #print(names)

    for j in names:
        if ( j == " "):
            count += 1
    print("The number of words in the string: ", count)


name = input("Please enter the string to find number of words in it: ")
numOfWord(name)