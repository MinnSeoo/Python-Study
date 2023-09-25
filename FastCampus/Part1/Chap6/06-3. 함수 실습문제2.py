# 함수 실습문제
# "로또 예상번호 추출 프로그램" 만들기!
# [조건]
# 1. 로또 번호를 6개 생성
# 2. 로또 번호는 1 ~ 45중 랜덤한 숫자이다.
# 3. 로또 번호는 각각 다른 숫자이여야 한다.
# 4. getRandomNumber() 함수를 사용해서 구현한다.


import random   # random 함수를 import

LottOfList = []  # random 숫자를 받아와서 저장할 list 선언
count = 0       # list에 값을 몇개 넣었는지 확인하는 변수

# 함수 선언
def get_random_number():
    number = random.randint(1,45)   # number 변수에 1 ~ 45 까지의 랜덤한 숫자 1개를 추출해서 저장
    return number   # number 변수 반환


# while 문이 True인 동안에
while True:
    if count > 5:   # 문제에서 6개의 숫자를 저장하라고 했으므로 count 0 ~ 5까지 -> count가 5보다 커지면 x
        break       # while 문 종료
    randomNum = get_random_number()   # 그렇지 않다면 randomNum에 get_random_number 함수 호출하여 값을 저장

    if randomNum not in LottOfList:  # 문제에서 중복된 값은 허용x -> 로또 리스트에 중복값이 들어가지 않았는지 확인
        LottOfList.append(randomNum) # 현재 LottOfList 리스트의 마지막 인자로 전달된 값을 추가.
        count += 1                  # cnt 횟수 증가.

LottOfList.sort()    # 숫자를 오름차순으로 정렬
print(LottOfList, "") # LottoOfList를 출력!
