
string1 = "Hello Raja"
string2 = "Hello Ravi"

name1 = []
name2 = []

for i in string1:
    name1.append(i)
print(name1)

for j in string2:
    name2.append(j)
print(name2)


s = (set(string1)&set(string2))

for k in s:
    print(k)



