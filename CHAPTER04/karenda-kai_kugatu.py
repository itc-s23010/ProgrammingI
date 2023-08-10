s1 = "{:>4s}{:>4s}{:>4s}{:>4s}{:>4s}\033[32m{:>4s}\033[0m\033[31m{:>4s}\033[0m".format(
    "Mon", "Tue", "Wed", "Thr", "Fri", "Sat", "Sun"
)
s1 += "\n"
s2 = "{:16s}".format(" ")
for i in range(1, 31):
    if i % 7 == 2:
        s2 += "\033[32m{:>4s}\033[0m".format(str(i))
    elif i % 7 == 3:
        s2 += "\033[31m{:>4s}\033[0m".format(str(i))
        s2 += "\n"
    else:
        s2 += "{:>4s}".format(str(i))
print(s1 + s2)
