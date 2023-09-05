# raise 구문 사용 -> 에러 강제 발생 시키기!

# 방법1
try:
    number = int(input("음수를 입력해 주세요 : "))
    if number >= 0:
        raise Exception("양수는 입력불가")
except Exception as e:
    print("에러발생!", e)



#------------------------------------------------

# 방법2
# 내장되어있지 않은 에러를 발생시킬 수도 있다. -> 새로 생성함.

class PositiveNumberError(Exception):
    def __init__(self):
        super().__init__("양수는 입력 불가")
        

try:
    number = int(input("음수를 입력해 주세요 : "))
    if number >= 0:
        raise PositiveNumberError
except PositiveNumberError as e:
    print("에러 발생",e)