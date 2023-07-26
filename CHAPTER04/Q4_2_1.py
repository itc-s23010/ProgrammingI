def number_to_day(num=1):
    if num == 0:
        day = "今日"
    elif num == 1:
        day = "明日"
    elif num == -1:
        day = "昨日"
    else:
        day = "今日より１日を超えて離れた日"
    return day
