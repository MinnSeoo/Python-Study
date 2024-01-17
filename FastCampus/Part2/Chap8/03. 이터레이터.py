# 이터러블 객체란 ? -> 순서가 있는 자료형 
# ex) for in 문에 사용함
# 대표적으로 문자열, 리스트, 튜플, 딕셔너리, range 객체..등

# 생성 방법! 
# 1) 이터레이터 클래스를 정의
# 2) __iter__ 메서드를 정의
# 3) __nex__ 메서드를 정의

# for i in "123":
#     print(i)
    
# for i in [11, 22, 33]:
#     print(i)
    
print(dir([10, 20, 30]))    # -> 리스트에는 어떠한 객체들이 존재하는지 확인함 -> 이중 이번 수업에서는 __iter__ 객체의 대하여 살펴보겠음.

print(type([10, 20, 30].__iter__))  # iter의 객체의 타입을 출력함 -> 결과 : method-wrapper

iter_obj = [10,20,30].__iter__()    
print(iter_obj)                     # 출력결과 list형태의 iter 객체인것을 확인할 수 있음.

# ----------------------
# iter한 리스트에는 __next__ 라는 메서드가 존재한다.
# 우리는 이 next 메서드를 통해서 for in문에 값을 하나씩 할당한다.
print(iter_obj.__next__())  # 10
print(iter_obj.__next__())  # 20
print(iter_obj.__next__())  # 30