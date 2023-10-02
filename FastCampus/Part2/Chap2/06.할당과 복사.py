a = [1,2,3,4,5]
b = a
b[0] = 10       # 나는 b의 값만 변경하고 싶었음
print(a)        # 출력결과 a의 값 까지 변경됨.
print(b)        # a,b는 서로 같은 데이터를 가리키고 있기 때문에 둘중 하나의 값만 변경해도 둘 다 적용이 됨.
print(id(a))    # a의 주소값 출력
print(id(b))    # b의 주소값 출력 

# 위와 같은 경우를 해결하기 위해서 copy를 사용함!

x = [1,2,3,4,5]
y = x.copy()    # copy를 사용하면 x와 다른 또 다른 객체 y가 생성됨
y[0] = 10       # 따라서 y의 값을 변경해도
print(x)        # x에는 영향을 미치지 않는다!
print(y)
print(id(x))    # 그렇기 때문에 주소 값도 다른것을 알 수 있다
print(id(y))


# 만약 다차원 리스트를 복사 하고 싶으면 ?
import copy
x1 = [[1,2], [3,4,5]]
y1 = copy.deepcopy(x1)  # copy 모듈을 import 한 후 deepcpy 함수를 사용해야함! 
y1[1][0] = 30
print(x1)
print(y1)
print(id(x1))
print(id(y1))

