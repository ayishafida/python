num = int(input("Enter number of steps:"))
for i in range(1, num+1):
    for j in range(1, i+1):
        print(i * j, end='\t')
    print(end='\n')