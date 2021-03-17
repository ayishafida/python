s = input("Enter a string:")
# x = s.split()
if s.endswith("ing"):
    a = s + "ly"
else:
    for i in s:
        if s[-1] != 'e':
            a = s + "ing"
        else:
            sliced = s.rstrip(s[-1])
            a = sliced + "ing"
print(a)