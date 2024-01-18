# 데코레이터란 ? -> 함수의 앞,뒤로 부가적인 기능을 넣어 주고 싶을 때 사용
# ex) 로깅, 권한 ..등

# 생성 방법
# 1) 클러저 이용
# 2) 적용하고 싶은 함수앞에 @(데코레이터) 사용

# 데코레이터 생성
def logger(func):
    def wrapper(arg):
        print("함수 시작")
        func(arg) # 함수 실행
        print("함수 끝")
    return wrapper

@logger
def print_hello(name):
    print("hello ", name)

@logger
def print_bye(name):
    print(f"good by {name}! /n see you next time:)")
    
    
print_hello("everyone!")
print_bye("Jon")