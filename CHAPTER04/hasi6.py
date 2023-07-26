pairs = [
    (2, "down"),
    (1, "up"),
    (4, "charm"),
    (3, "strange"),
    (6, "top"),
    (5, "bottom"),
]
pairs.sort(key=lambda x: x[0])
print(pairs)
