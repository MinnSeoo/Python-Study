# map 함수 사용방법
# map(함수, 순서가있는자료형)
# map(int['3','4','5','6'])   # 이 경우 map object에 리스트 들이 저장이 됨.

# 파이썬에서는 map 객체를 다루기 조금 껄끄러움
# 따라서 map 객체를 list 형으로 형 변환을 해 주는 것이 좋음!
# list(map(함수, 순서가있는자료형))
# list(map(int['3','4','5','6']))


# map 함수를 통해서 리스트 모든 요소의 공백을 제거 해 보자

# for문을 사용한 case
books = [' 혼공파 ', ' 혼공C ']
print(books)

for i in range(len(books)):
    books[i] = books[i].strip()
    
print(books)


# map 함수를 사용한 case
def strip_all(f):
    return f.strip()

fruits = [' apple ', ' peach ']
print(fruits)

fruits = list(map(strip_all, fruits))
print(fruits)

# lambda 함수 + map 함수
items = [' 맥북_Air ', ' 아이폰14 ']
print(items)

items = list(map(lambda item : item.strip(), items))
print(items)


# filter 함수 사용 방법
# filter(함수, 순서가있는자료형)
def function(x):
    return x < 0 
filter(function,[0,1,2,3,-4])

# 리스트에서 길이가 3 이하인 문자들만 필터링

#  for문 사용
animals = ['cat', 'tiger', 'dog', 'bird', 'monkey']
result = []
for i in animals:
    if len(i) <= 3:
        result.append(i)

print(result)

# filter 함수 사용
def func(x):
    return len(x) <= 3

print(list(filter(func, ['one', 'two', 'three', 'four', 'five'])))


# lambda 함수 + filter 함수
name_list = ['John', 'Sara', 'Son', 'Medison', 'Barb', 'Kaile']
about_name = list(filter(lambda name: len(name) <= 5, name_list))
print(about_name)
 