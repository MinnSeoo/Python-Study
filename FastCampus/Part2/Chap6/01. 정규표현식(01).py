import re 

# 1. re 모듈 메서드

str  = 'Hi My name is Minseo, My name is six letter and I like my name!'

# 1) match : 문자열의 처음부터 검색. -> 결과 : 한개의 match 객체가 출력됨.
result = re.match('name', str)      # str이 name으로 시작하지 않으므로 none 반환
print(result)

result = re.match('Hi', str)
print(result)

# 2) search : 문자열의 전체를 검색. -> 결과 : 한개의 match 객체가 출력됨.
result = re.search('like', str)
print(result)

# 3) findall : 문자열의 전체를 검색 -> 결과 : 문자열 리스트가 출력됨.
result = re.findall('name', str)
print(result)

result = re.findall('six', str)
print(result)


# 4) finditer : 문자열 전체를 검색 -> 결과 : match 객체 이터레이터
result = re.finditer('Minseo ',str)
print(result)


results = re.finditer('name', str)
print(result)

for result in results:
    print(result)
    

# 5) fullmatch : 패턴과 문자열이 완벽하게 일치하는지 검사
str2 = 'Learing Python is fun!'
result = re.fullmatch('Learing Python is fun!', str2)
print(result)

result = re.fullmatch('Learing python is fun!', str2)       # 일치하지 않을 경우 None 반환
print(result)

# 2. match object의 메서드
result = re.search("Python", str2)

# 1) group() : 매칭된 문자열을 반환 
print(result.group())

# 2) start() : 매칭된 문자열의 시작 위치 반환
print(result.start())

# 3) end() : 매칭된 문자열의 끝 위치 반환
print(result.end())

# 4) span() : 매칭된 문자열의 (시작, 끝) 위치 튜플을 반환
print(result.span())