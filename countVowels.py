# Task 5- Question -1- Calculate total number of vowels
name = "Guvi Geeks Network Private Limited"
count = 0
for m in name:
    print(m, end = "")
    if (m == "a" or m == "e" or m == "i" or m == "o" or m == "u"):
        count += 1
print("\n")
print("The total number of vowels:", "=", count)

