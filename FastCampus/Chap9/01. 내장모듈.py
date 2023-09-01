# 내장 모듈
# 파이썬 설치시 자동으로 설치되는 모듈들을 뜻함
# ex) import math 

import math
print(math.pi)  # 위와같이 모듈명 . 사용할 변수 및 함수의 명을 써주면 된다.
print(math.ceil(3.8))       


from math import pi, ceil   # 위의 방법이 귀찮으면 이 방법을 사용해도 값은 같음.
print(pi,"\n",ceil(3.8))


# 외부 모듈
# 다른 사람이 만들어둔 파이썬 파일을 pip로 설치해서 사용함.
# pyautogui -> 매크로 모듈을 이번 실습에서 사용하겠음.
# 가상환경에서 python3 install pyautogui -> 설치해줌 
# (이번 실습은 다른 폴더에 존재하는 가상환에 설치후 실습 진행하였기에 간단하게 정리만 하겠음.)

import pyautogui as pg
pg.moveTo(500, 500, duration=2) # 화면의 x,y의 500위치에 2초동안 마우스를 이동해라.

