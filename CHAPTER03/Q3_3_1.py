my_list = ["tokyo", "osaka", "fukuoka", "aichi", "kyoto", "chiba", "saitama", "gunma"]
list_6 = []
# result = ([(list_6.append(s) in [len(s) >= 6] if [for s in my_list]])
for s in my_list:
    if len(s) >= 6:
        list_6.append(s)
print(list_6)
