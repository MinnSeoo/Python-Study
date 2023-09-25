# 생성자 실습
# 생성자 : 인스턴스를 만들 때 호출되는 호스트

class Monster:
    def __init__(self, health, attack, speed):
        self.health = health
        self.attack = attack
        self.speed = speed
    
    def decrease_health(self,num):
        self.health -= num
        
    def get_health(self):   # 현재 자기 자신의 체력을 반환 
        return self.health
        
# 고블린 인스턴스 생성
goblin = Monster(800, 60, 300)
goblin.decrease_health(100)
print(goblin.get_health())


# 늑대 인스턴스 생성
wolf = Monster(1000,200,500)
wolf.decrease_health(500)
print(wolf.get_health())
