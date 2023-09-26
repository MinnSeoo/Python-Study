# 소문자를 대문자로 바꾸는 방법
my_self = "Hi i'm MinsEo jUng"
print(my_self.upper())

# 대문자를 소문자로 바꾸는 방법
my_self = "Hi i'm MinsEo jUng"
print(my_self.lower())

# 문자열 바꾸는 방법
today_weather = "오늘 날씨는 매우 흐림 입니다."
print(f"처음 값 :{today_weather}")
today_weather.replace("흐림", "맑음")    # 첫 번째 인자에는 바꾸고 싶은 문자열을, 두 번째 인자에는 바꿀 문자열을 작성
print(f"변경 후 : {today_weather}")

# 문자열 위치 찾는 방법
print("Hello World!".find("World!"))    # 'W'가 작성되어있는 인덱스 번호를 반환함. / 만약 해당하는 문자열이 없을경우 -1을 반환.

# 문자열 개수 세는 방법
print("Hi By Hi By Hi By Hi By By By".count("By"))

# 문자열을 분리하는 방법
print("뉴발티셔츠 M 29000".split)

# 콜론을 기준으로 문자 분리하기!
print("뉴발티셔츠:M:29000".split(':'))

# 문자열을 연결하는 방법
print(''.join(['뉴발신발', ' 240mm', ' 32000₩', ' 기종 : X89076']))

# 공백 삭제하는 방법
# lstrip() -> 왼쪽 공백 삭제
# rstrip() -> 오른쪽 공백 삭제
# strip() -> 모든 공백 삭제


