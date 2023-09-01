# Task-5 - Question -8 Find Anagram
def findAnagram(name1, name2):
    lengthOfName1 = len(name1)
    lengthOfName2 = len(name2)
    #print(lengthOfName1)
    #print(lengthOfName2)

    if(lengthOfName1 == lengthOfName2):
        m = sorted(name1)
        n = sorted(name2)
        print(m)
        print(n)
        if (m == n):
            return "True"
        else:
           return "False"

name1 = input("Please enter the first string: ")
name2 = input("Please enter the second string: ")
name1 = name1.lower() # change to lower case
name2 = name2.lower()
print(findAnagram(name1, name2))



