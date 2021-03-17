text = "this is the that of is this is the"
d = dict()
words = text.split()
for w in words:
    if w in d:
        d[w] = d[w]+1
    else:
        d[w] = 1
for key in list(d.keys()):
    print(key, ":", d[key])