def make_addfunc():
    def add(x, y):
        return x + y

    return add


adder = make_addfunc()
answer = adder(1, 10)
print(answer)
