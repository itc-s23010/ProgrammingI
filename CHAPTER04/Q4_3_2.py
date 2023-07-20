def func_square(*ahaha):
    results = []
    for n in ahaha:
        results.append(n * n)
    return results


numbers = [1, 2, 3, 4]
print(func_square(*list(range(100))))
