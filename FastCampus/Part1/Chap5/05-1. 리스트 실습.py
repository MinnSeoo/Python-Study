# 1) 다음은 O O 고등학교 2학년 1반 1번 ~ 5번까지의 1분간 팔굽혀펴기 개수이다.
#    데이터는 리스트에 저장되어있다. 각 조건을 실행한 결과를 출력해 보자.

# result = [33, 40, 12, 63, 52]

# [조건1] - 6번의 팔굽혀펴기 개수는 9개이다. 리스트의 맨 마지막에 추가해 보자.
result = [33, 40, 12, 63, 52]

result.append(9)

print(result)

# [조건2] - 2번은 재측정하여 50개를 하였다. 2번 데이터 값을 변경해 보자.
result[1] = 50
print(result)

# [조건3] - 3번부터 6번까지의 데이터를 슬라이싱하자.
print(result[2:])

# [조건4] - 모든 데이터를 오름차순으로 정렬하자.
result.sort()
print(result)


# 2) 턱걸이 평균 측정 프로그램을 만들어보자. 먼저 턱걸이 횟수를 저장할 빈 리스트를 만든다.
#    그리고 일주일간의 턱걸의 횟수를 입력받아 리스트에 저장한다. 리스트에 저장된 데이터의 평균을 구해 출력한다.
data = []
total = 0

cnt  = int(input("1일차 턱걸이 횟수 : ")) 
data.append(cnt)

cnt  = int(input("2일차 턱걸이 횟수 : ")) 
data.append(cnt)

cnt  = int(input("3일차 턱걸이 횟수 : ")) 
data.append(cnt)

cnt  = int(input("4일차 턱걸이 횟수 : ")) 
data.append(cnt)

cnt  = int(input("5일차 턱걸이 횟수 : ")) 
data.append(cnt)

cnt  = int(input("6일차 턱걸이 횟수 : ")) 
data.append(cnt)

cnt  = int(input("7일차 턱걸이 횟수 : ")) 
data.append(cnt)

total = data[0] + data[1] + data[2] + data[3] + data[4] + data[5] + data[6]

print("평균 : {}".format(total / 7))

# 위와 같이 나타내면 코드수정 할때 불편하다.
# 그렇기 때문에 반복문을 통해서 위와 같은 결과를 출력해 보겠다.
# range 함수를 통해서 리스트를 따로 만들지 않아도 내가 지정한 범위를 나타낼 수 있다.
data = []

for i in range(1,101):
    cnt  = int(input(i, "일차 턱걸이 횟수 : "))
    data.append(cnt)
    


