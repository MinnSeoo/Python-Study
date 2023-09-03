# 1. 파이썬 객체를 pickle로 저장하기
# pickle은 텍스트 상태의 데이터가 아닌 파이썬 객체 자체를 파일로 저장하는 역할을 한다.

import pickle
data = {
    "목표1 : 매일 코딩 공부 1시간 이상",
    "목표2 : 매일 ToDo로 계획 세우기",
    "목표3 : 주말에도 열심히 달리기"
}

file = open("./FastCampus/Chap10/data.pickle", "wb")
pickle.dump(data, file)     # dump 함수를 이용해 객체 상태의 데이터를 바이너리 형태로 변환한다.
file.close()

# 2. pickle 파일을 파이썬으로 가져오기 
file = open("data.pickle", "rb")    # -> 읽기 모드
data = pickle.load(file)
print(data)
file.close("./FastCampus/Chap10/data.pickle", "rb")

#---------------------------------------------------------------------------------

# with 구문
# with 구문을 사용하면 자동으로 파일을 닫아준다.
with open("./FastCampus/Chap10/data.txt", "r", encoding="utf8") as file:    # 읽기 모드
    data = file.read()
    print(data)
    

# school.txt 파일을 w 옵션으로?
# w 옵션은 파일을 쓰기 모드로 열고, 만약 해당 파일이 이미 존재한다면 그 파일을 덮어쓴다.
# -> 즉, 새로운 파일을 생성하거나 이미 존재하는 파일의 내용을 대체한다.
# 반면 a 옵션은 파일을 쓰기 모드로 열되, 파일이 존재한다면 수정한 내용을 기존의 내용 끝에 이어서 쓴다.
with open("./FastCampus/Chap10/school.txt", "w", encoding="utf8"):
    data = file.write()
    print(data)


# --------------------------------------------------------------------------------
# csv 파일이란 ? 
# comma separated variables의 약자로, 텍스트 파일 형식의 데이터를 저장하는데 사용된다.

# csv 파일 쓰기
import csv
data = [
    ["이름", "반", "번호"],
    ["재석", 1, 1],
    ["하하", 2, 22],
    ["소민", 3, 13]
]

file = open("./FastCampus/Chap10/student.csv", "w", encoding="utf8")    # 파일을 덮어쓰기 모드로 열어준다. -> 없으면 생성한다.
writer = csv.writer(file)   # writer 변수에 csv형식의 데이터를 파일에 쓸 수 있는 writer 객체를 생성후 저장한다.

for d in data:      # d에 data 리스트의 값이 한 개 씩 저장된다. 
    writer.writerow(d)  # 리스트로 저장된 데이터가 csv 파일에 한 줄 씩 저장된다.

file.close()


# csv 파일 읽기
import csv
open("./FastCampus/Chap10/student.csv", "r", encoding="utf8")   # student.csv 파일을 읽기 모드로 연다.
reader = csv.reader(file)   # reader 변수에 csv형식의 데이터를 파일을 읽을 수 있는 reader 객체를 생성후 저장한다.

for data in reader:     # reader 변수에 저장되어 있는 데이터 값들을 1개씩 출력함.
    print(data)
file.close()
    