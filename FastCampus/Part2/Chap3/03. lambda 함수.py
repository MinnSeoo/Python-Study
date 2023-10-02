# lambda 함수란 ? 
# -> 이름을 지을 필요도 없을 간단한 형태의 함수
# -> 다른 함수의 인자(argument)로 넣을 수 있다.
# -> 장점 : 코드가 간결해 지고, 메모리가 절약된다.

# lambda 함수 정의 방법
# lambda 매개변수 : 결과
lambda a : a-1

# lambda 함수 호출 방법
# 방법1 -> 함수 자체를 호출
(lambda a : a-1)(10)   

# 방법2 -> 변수에 담아서 호출
minus_one = (lambda a : a -1)
minus_one(10)                # 변수를 함수처럼 호출해서 사용함.


# lambda 함수 사용방법 -> if문

# 사용 하지 않을 경우
def is_positive_number(a):
    if a > 0:
        return True
    else: 
        return False
    
# 함수 호출 
is_positive_number(-2)

# 사용할 경우
lambda a : True if a > 0 else False     # 코드가 훨씬더 간결해 진다!

# 함수 호출! 
(lambda a : True if a > 0 else False)(-2)