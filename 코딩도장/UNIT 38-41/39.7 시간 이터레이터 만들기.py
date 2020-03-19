# 표준 입력으로 정수 세 개가 입력됩니다
# (첫 번째 정수는 시작하는 초, 두 번째 정수는 반복을 끝낼 초, 세 번째 정수는 인덱스이며 입력되는 초의 범위는 0~100000, 입력되는 인덱스의 범위는 0~10입니다). 
# 다음 소스 코드에서 시간 값을 생성하는 이터레이터를 만드세요.

# 시간 값은 문자열이고 시:분:초 형식입니다. 만약 숫자가 한 자리일 경우 앞에 0을 붙입니다(예: 12:01:08).
# 1초는 00:00:01입니다. 23:59:59를 넘길 경우 00:00:00부터 다시 시작해야 합니다.
# 시간은 반복을 끝낼 초 직전까지만 출력해야 합니다(반복을 끝낼 초는 포함되지 않음).

# 0 3 2
# 00:00:00
# 00:00:01
# 00:00:02
#
# 00:00:02

# 88234 88237 1
# 00:30:34
# 00:30:35
# 00:30:36
#
# 00:30:35

class TimeIterator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.index_stop = stop - start


    def __getitem__(self, index):
        if index < self.index_stop:
            time = self.start + index
            if time >= 86400:
                time -= 86400
                
            sec = time % 60
            minute = (time % 3600) // 60
            hour = time // 3600
            return '{0:02d}:{1:02d}:{2:02d}'.format(hour, minute, sec)
        else:
            raise IndexError



start, stop, index = map(int, input().split())

for i in TimeIterator(start, stop):
    print(i)

print('\n', TimeIterator(start, stop)[index], sep='')