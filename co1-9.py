s = input("Enter a string:")
end = s[-1]
start = s[0]
ns = end + s[1:-1] + start
#ns = s.replace(s[0], s[-1]) and s.replace(s[-1], s[0])
print(ns)