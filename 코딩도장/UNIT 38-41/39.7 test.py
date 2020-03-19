value = 3
hour = 0
minute = 0
sec = 0

# 23:59:59 이상 일때 00:00:00 으로 넘기기
if value >= 86400:
    value -= 86400

print(value)

# '초'로 주어진 시간 시:분:초 로 만들기
sec = value % 60
minute = (value - sec) // 60

if minute >= 60:
    hour = minute // 60
    minute = minute - hour*60

print(hour, minute, sec, sep=':')
print('{0:02d}:{1:02d}:{2:02d}'.format(hour, minute, sec))