f=open("demo.txt", "r")
l=[]
for x in f:
    l.append(x)
f.close
print(l)