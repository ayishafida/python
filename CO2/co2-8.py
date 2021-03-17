l = []
limit = int(input("Enter limit:"))
for i in range(limit):
    element = input("Enter list of words:")
    l.append(element)
longest = max(l, key=len)
len = len(longest)
print("The longest word id:", longest)
print("The length of the longest word is:", len)
