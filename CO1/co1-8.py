s = input("Enter a string:")
b = s[0]
for i in s:
    if i == b:
        s = s.replace(i, "$")
print(b + s[1:])