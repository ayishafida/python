s = input("Enter a string:")
d = {}
for x in s:
    if x in d:
        d[x] += 1
    else:
        d[x] = 1
print(d)