l1 = [3, 5, 8, 1, 26, 18]
l2 = [14, 23, 17, 9, 20, 8]
len1 = len(l1)
len2 = len(l2)
print("length of list1 is", len1)
print("length of list2 is", len2)
if len1 > len2:
    print("List 1 has bigger length than list 2")
elif len1 < len2:
    print("List 2 has bigger length than list 2")
else:
    print("Both lists have the same length")
print("\n")
s1 = sum(l1)
s2 = sum(l2)
print("List1 sum:", s1)
print("List2 sum:", s2)
if s1 > s2:
    print("List 1 has greater sum than List 2")
elif s2 > s1:
    print("List 2 has greater sum than List 1")
else:
    print("Lists sum to the same value")
print("\n")
l3 = []
for x in l1:
    if x in l2:
        if x not in l3:
            l3.append(x)
print("The value that occur in both the list are:", l3)


