# 표준 입력으로 시:분:초 형식의 시간이 입력됩니다. 
# 다음 소스 코드에서 Time 클래스를 완성하여 시, 분, 초가 출력되게 만드세요. 
# from_string은 문자열로 인스턴스를 만드는 메서드이며 
# is_time_valid는 문자열이 올바른 시간인지 검사하는 메서드입니다. 
# 시간은 24시까지, 분은 59분까지, 초는 60초까지 있어야 합니다. 
# 정답에 코드를 작성할 때는 class Time:에 맞춰서 들여쓰기를 해주세요.

# 23:35:59
# 23 35 59

# 12:62:43
# 잘못된 시간 형식입니다.

class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @staticmethod
    def is_time_valid(time_string):
        hour, minute, second = map(int, time_string.split(':'))
        return hour <= 24 and minute <= 60 and second <= 60

    @classmethod
    def from_string(cls, time_string):
        hour, minute, second = map(int, time_string.split(':'))
        time = cls(hour, minute, second)
        return time
        

        


time_string = input()

if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')