# 파일 입출력을 사용하는 이유 ?
# 1. 파일로부터 데이터를 읽어와 프로그램에 사용하기 위해.
# 2. 프로그램에서 만든 데이터를 파일형태로 저장하기 위해.

# 파일 열기 모드에는? 
# w : 쓰기
# a : 추가
# r : 읽기 
# (보통은 파일 열기 -> 작업 -> 저장 순으로 작업이 진행된다.)


# 파일 쓰기 == w    -> 덮어쓰기
# data.text 파일을 쓰기모드로 연다. (없으면 파일을 생성함.) 그 다음 파일 객체를 file 변수에 담는다.
# encoding 방식을 utf8로 지정해 한글로 불러오도록 한다.
file = open("./FastCampus/Chap10/data.text", "w", encoding="utf8")   
file.write("1.파이썬 공부는 정말 재밌다...!")   # 파일 데이터를 수정
file.close()

# 파일 추가 == a    -> 이어쓰기
file = open("./FastCampus/Chap10/data.text", "a", encoding="utf8")
file.write("\n2. 이 재밌는걸 안한다고...?")
file.close()


# 파일 읽기 == r
file = open("./FastCampus/Chap10/data.text", "r", encoding="utf8")

# 3.1 파일 전체 읽기
data = file.read()
print(data)
file.close()

# 3.2 파일 한 줄 읽기
while True:
    data = file.readline()  # readline() 함수는 file의 있는 데이터들을 한줄씩 읽는 역할을 한다.
    print(data, end="")     # 객체에 저장된 내용을 출력, end="" 를 통해 줄바꿈을 없애줌.
    if data == "":          # 만약 data에 읽을 문자가 없을경우, 공백일 경우
        break               # 종료
file.close()                # 파일 닫기.


