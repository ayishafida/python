n = int(input("enter limit:"))
list = []
for x in range(n):
    x = int(input("enter nos:"))
    list.append(x)
print(list)
square = [x*x for x in list]
print(square)