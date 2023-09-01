# Task-5- Question-5 - function to write palindrome or not

def palindrome(name):
    lists =[]
    revName = []
    results = []

    for i in name:
        lists.append(i)
    #print(lists)
    length = len(lists)
    #print(length)

    for i in range(1, length+1):
        #print(lists[length-i])
        c = lists[length-i]
        print(c, end="")
        # reverse the entered string
        revName.append(c)
    #print(revName)
    print("\n")

    for i in range (0, length):
        if lists[i] == revName[i]: #Compare entered and reversed string
            results.append("T")
        else:
            results.append("F")
    #print(results)

    if "F" in results:   # Check anything false in the array. Then print false
        print( "False not a palindrome")
    else:
        print("True it is a palindrome")

name = input("Please enter name to find palindrome or not: ")
name = name.lower()
palindrome(name)
    




