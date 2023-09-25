# 튜플
# : 읽기 전용 리스트
a = (3, 4, 5)
print(a)

# 괄호 생략 가능!
b = 3, 4, 5  
print(b)

# c = (3)   // <- 이 코드는 C라는 변수에 3을 대입하는것 이기 때문에 튜플이 X
# 튜플안에 값을 1개만 주고 시작하고 싶을때는 반드시 `,` 을 붙여줘야함!
c = (3,)
print(c)

d = tuple([1,2,3])      # tuple 이라는 함수를 사용해 리스트를 튜플로 변환 가능!
print(d)

e = list(range(10))     # list or tuple에 range 객체 사용 가능!
print(e)

f = tuple(e)            # e를 tuple로 변경.
print(f)

g = 3,4,5
h = list(g)
print(g)

# 튜플 관련 함수
x = 5, 6, 7, 8

print(max(x))
print(min(x))
print(sum(x))
