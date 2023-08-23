# 오버라이딩 실습

# 클래스 변수 : 클래스 내 인스턴스 모두 공유하는 변수.

import random

# 부모 클래스
class Monster:
    max_num = 1000  # 몬스터 클래스 변수
    def __init__(self, name, attack, speed):
        self.name = name
        self.attack = attack
        self.speed = speed
        Monster.max_num -= 1    # 생성자가 실행될때마다 max_num을 1씩 차감한다.
    def move(self):
        print(f"[{self.name}] 지상에서 이동하기")
        

# 자식 클래스
class Wolf(Monster):    # 몬스터 클래스를 그대로 상속받는다.
    pass

class Shark(Monster):
    def move(self): # 메서드 오버라이딩
        print(f"[{self.name}] 헤엄치기")
        
class Dragon(Monster):
    # 생성자 오버라이딩
    def __init__(self, name, attack, speed, skill=""):  # skill의 기본값 지정해야 오류가 발생하지 않음.
        super().__init__ (name, attack, speed)  # 부모 클래스의 init 함수를 불러옴
        self.skills = ("화염", "고속비행", "꼬리치기")
        
    def move(self): # 메서드 오버라이딩
        print(f"[{self.name}] 헤엄치기")
        
    def skill(self):
        print(f"[{self.name}] 스킬을 사용하였다 -> {self.skills[random.randint(0,2)]}")   # 스킬 3가지 중 랜덤으로 1가지만 출력되도록 함.
        

wolf = Wolf("늑대", 300, 500)   # 함수에 전달할 인자 값을 지정해 준다.
wolf.move() 
print(wolf.max_num)
 
shark = Shark("상어", 500, 600)
shark.move()
print(shark.max_num)

dragon = Dragon("용", 1000, 700)
dragon.move()
dragon.skill()
print(dragon.max_num)

  