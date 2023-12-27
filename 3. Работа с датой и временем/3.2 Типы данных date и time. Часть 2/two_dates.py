from datetime import date

dt1, dt2 = date.fromisoformat(input()), date.fromisoformat(input())
print(min(dt1, dt2).strftime('%d-%m (%Y)'))
