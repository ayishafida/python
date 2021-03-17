import math
perfect = []
start = int(input("Enter starting range:"))
end = int(input("Enter ending range:"))
for i in range(start, end+1):
    flag = 0
    num = i
    while num > 0:
        digit = num % 10
        if digit not in [0, 2, 4, 6, 8]:
            flag = 1
            break
        num = int(num / 10)
    if flag == 0 and int(math.sqrt(i)+0.5)**2 == i:
        perfect.append(i)
print("The list of perfect squares are", perfect)
# if start % 10 and not(start / 10000) and start / 1000 and start / 100 and start / 10:
#     if end % 10 and not(end / 10000) and end / 1000 and end / 100 and end / 10:
#     else:
#         print("Ending range not in 4 digits")
# else:
#     print("Starting range not in 4 digits")