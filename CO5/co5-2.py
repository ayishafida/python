f = open("1.txt", "r")
c = open("2.txt", "w")
line = f.readlines()
type(line)
for i in range(0, len(line)):
    if i % 2 != 0:
        c.write(line[i])
    else:
        pass
c.close()
c = open("2.txt", "r")
line1 = c.read()
print(line1)
f.close()
c.close()