from datetime import date

dates = [date.fromisoformat(input()) for _ in range(int(input()))]
for dt in sorted(dates):
    print(dt.strftime('%d/%m/%Y'))
