# 리스트에 데이터를 추가하는 방법
fruits = ['apple', 'pinapple', 'strowberry']
fruits.append('grape')
print(fruits)

# 리스트에 리스트를 추가하는 방법
weekend = ['Saturday']
weekend.append(['Sunday'])
print(weekend)

# 리스트에서 데이터를 삭제하는 방법
# 1. pop() -> 괄호안 인덱스 번호 지정해 주면 해당하는 데이터 삭제 / 지정하지 않을시 리스트의 마지막 요소값 삭제됨.
test_list = ['test1','test2', 'test3']
print(test_list.pop())
print(test_list)

# 2. remove() -> remove 메서드 안에 데이터 값을 넣어주면 해당하는 데이터 값 삭제됨.
test_list.remove('test2')
print(test_list)

# 3. del()
test_list2 = ["Hi", "my", "name", "is", "John"]
del test_list2[0]
print(test_list2)

# 리스트의 특정 인덱스 값을 구하는 방법
print(fruits.index('apple'), fruits.index('pinapple'))

# 리스트의 개 수를 구하는 방법
alphabet = ('a','b','c','a','b','c','b')
print(alphabet.count('b'))

# 리스트를 정렬하는 방법
number = [1,3,6,2,4,7]
number.sort()
print(number)


# for in 반복문 사용할 때 인덱스를 같이 출력하는 방법
num_list = [10, 22, 13, 42, 35]
for index, num in enumerate(num_list):
     print(index, num)


Month = ["January", "February", "March", "April", "May"]
for index, Month in enumerate(Month,1): 
    print(f"{index}월은 {Month}")