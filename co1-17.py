d = {"h" : 2, "y" : 8, "a" : 21}
l = list(d.items())
l.sort()
print("Ascending order:", l)
l = list(d.items())
l.sort(reverse=True)
print("Descending order:", l)
