# 상속
# 클래스들에 중복된 코드를 제거하고 유지보수를 편하게 하기 위해 사용.

# 부모 클래스
class Monster:
    def __init__(self, name, attack, speed):
        self.name = name
        self.attack = attack
        self.speed = speed
    def move(self):
        print(f"{self.name} 지상에서 이동하기")
        

# 자식 클래스
class Wolf(Monster):    # 몬스터 클래스를 그대로 상속받는다.
    pass

class Shark(Monster):
    def move(self): # 메서드 오버라이딩
        print(f"{self.name} 헤엄치기")
        
class Dragon(Monster):
    def move(self): # 메서드 오버라이딩
        print(f"{self.name} 헤엄치기")
        

wolf = Wolf("늑대", 300, 500)   # 함수에 전달할 인자 값을 지정해 준다.
wolf.move() 
 
shark = Shark("상어", 500, 600)
shark.move()

dragon = Dragon("용", 1000, 700)
dragon.move()
        

  