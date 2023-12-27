from datetime import datetime, timedelta


def tmd2str(tmd):
    return f'{str(tmd.seconds // 3600).rjust(2, "0")}:{str((tmd.seconds // 60) % 60).rjust(2, "0")}'


h, m = map(int, input().split(':'))
start = timedelta(hours=h, minutes=m)

h, m = map(int, input().split(':'))
end = timedelta(hours=h, minutes=m)

lesson_duration = timedelta(minutes=45)
break_duration = timedelta(minutes=10)

result = []
cur_start = start

while end.total_seconds() - cur_start.total_seconds() >= lesson_duration.total_seconds():
    cur_end = cur_start + lesson_duration
    result.append((cur_start, cur_end))
    cur_start = cur_end + break_duration

print(*map(lambda td: f'{tmd2str(td[0])} - {tmd2str(td[1])}', result), sep='\n')
