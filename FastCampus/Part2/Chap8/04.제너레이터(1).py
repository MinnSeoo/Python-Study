# 제너레이터란? -> 이터레이터를 만드는 함수 (이터레이터를 간편하게 생성하는것?)
# -> 함수에서 yield를 사용해서 생성가능
# 특징 
# 1) 함수안에 yield 사용 
# 2) 제너레이터 표현식을 사용할 수 있다.
# 3) 메모리 사용 효율적!

# 1) yield 사용
def season_generator(*args):    # 인자값으로 가변 인수 넣어줌!  (함수 호출시 전달되는 인자 값이 가변적이라는 뜻)
    for arg in args:            
        yield arg               # yield를 사용하여 arg를 return하고 함수 실행을 잠깐 중단한다.(다음 함수가 호출되기 전까지 중단.)
        
g = season_generator('spring', 'summer', 'autum', 'winter')

print(g)        # 출력결과 -> 제너레이터 객체라고 나옴
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())


def func():
    print("1.작업중")
    yield 1
    
    print("2. 작업중")
    yield 2
    
    print("3. 작업중")
    yield 3
    
    
ge = func()
data = ge.__next__()
print(data)

data = ge.__next__()
print(data)

data = ge.__next__()
print(data)

# return과 yield의 차이점 
# return 사용시 return 만나면 함수 종료후 바로 결과값 반환 
# but yield 사용시 값을 return 후 함수 실행을 잠깐 중단함.


# -----------------------------------------------

# 2. 제너레이터 표현식 사용.
double_generator = (i * 2 for i in range(1,10))         # 리스트 생성시 대괄호 사용[], but 제너레이터 생성시 괄호 사용 ()
print(double_generator)      # 출력시 제너레이터 객체라고 나옴

for i in double_generator:
    print(i)


