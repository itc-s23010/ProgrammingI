import calendar
from datetime import datetime

today = datetime.today().date()


def create_calendar(year, month):
    cal = calendar.monthcalendar(year, month)
    youbi = ["月", "火", "水", "木", "金", "土", "日"]

    for i in youbi:
        if i == "土":
            print("\033[34m" + i + "\033[0m", end=" ")
        elif i == "日":
            print("\033[31m" + i + "\033[0m", end=" ")
        else:
            print(i, end=" ")
    print()

    for syuu in cal:
        for hi in syuu:
            if hi != 0:
                if calendar.weekday(year, month, hi) == 5:
                    print("\033[34m" + str(hi).rjust(2) + "\033[0m", end=" ")
                elif calendar.weekday(year, month, hi) == 6:
                    print("\033[31m" + str(hi).rjust(2) + "\033[0m", end=" ")
                else:
                    print(str(hi).rjust(2), end=" ")
            else:
                print("  ", end=" ")
        print()


create_calendar(today.year, today.month)
