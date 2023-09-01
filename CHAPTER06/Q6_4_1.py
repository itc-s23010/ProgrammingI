f = open("some.txt")
c = 0
for l in f:
    print(l, end="")
    if c == 2:
        break
    c += 1
f.close()
