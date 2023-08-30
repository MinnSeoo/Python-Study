# 원하는 메모를 파일에 저장하고 추가 및 조회가 가능한 간단한 메모장을 만들어 보자!
# 필요한 기능? -> 메모 추가 및 조회
# 입력받는 값 -> 메모 내용, 프로그램 실행 옵션
# 출력하는 값 -> memo.txt

# 가장 먼저 해야할 일 -> memo를 추가하는 것.

# sys.argv는 프로그램을 실행할 때 입력된 값을 읽어 들일 수 있는 파이썬 라이브러리이다.

import sys

option = sys.argv[1]


if option == '-a':      # 옵션이 'a'인 경우에만 실행 
    memo = sys.argv[2]  # memo변수에 memo.txt의 내용을 저장
    f = open('memo.txt', 'a')   # a 옵션으로 파일 연 후 f 변수에 저장
    f.write(memo)   # f 객체로 memo 변수 내용을 추가로 작성해 준다.
    f.write('\n')   # 줄바꿈 
    f.close         # 파일 닫기
    
elif option == '-v':        # 옵션이 'v'인 경우에만 실행
    f = open('memo.txt', 'v')   # f 변수에 memo.txt를 출력 모드로 연 후 저장
    memo = f.read()     # memo 변수에 f 객체를 읽기 모드로 저장
    f.close()           # 파일 닫기
    print(memo)         # 출력
    
sys.argv[0] # 파일제목
sys.argv[1] # 해당 파일에 들어갈 내용들 