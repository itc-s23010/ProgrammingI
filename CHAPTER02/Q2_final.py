import random
import string

while True:
    alp = random.choice(list(string.ascii_lowercase))
    print(alp)

    if alp == "k":
        break
