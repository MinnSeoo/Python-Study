# 클래스를 사용하는 이유
# 1. 코드 작성이 더 간편하다
# 2. 반복되는 작업을 수정할때 더 편리하다.

champion1_name = "이즈리얼"
champion1_health = 700
champion1_attack = 90

print(f"{champion1_name}님 소환사의 협곡에 오신것을 환영합니다.")


champion2_name = "리신"
champion2_health = 800
champion2_attack = 95

print(f"{champion2_name}님 소환사의 협곡에 오신것을 환영합니다.")


champion3_name = "야스오"
champion3_health = 1000
champion3_attack = 80

print(f"{champion3_name}님 소환사의 협곡에 오신것을 환영합니다.")


def basic_attack(name, attack):
    print(f"{name} 기본공격 {attack}")


basic_attack(champion1_name, champion1_attack)
basic_attack(champion2_name, champion2_attack) 

# 클래를 사용한 경우
print("================== 클래스를 사용한 경우 ===================")

class Champion:
    def __init__(self, name, health, attack):   # __init__ 메서드는 Champion 클래스의 생성자 이다. 
        self.name = name                        # 생성자의 인자값으로 self가 있는데 이는 인스턴스 자신을 나타내는 매개변수이다.
        self.health = health
        self.attack = attack
        print(f"{name}님 소환사의 협곡에 오신걸 환영합니다.")
    
    def basic_attack(self):
        print(f"{self.name} 기본공격 {self.attack}" )
    
ezrial = Champion("이즈리얼", 700, 90)
leesin = Champion("리신", 800, 95)
yasuo = Champion("야스오", 1000, 80)

ezrial.basic_attack()
leesin.basic_attack()
yasuo.basic_attack() 


# 클래스는 속성과 메서드로 이루어진다. 
# 이때 이 속성은 특징을 나타내고, 메서드는 동작들을 나타낸다.

# 파이썬에서는 자료형도 클래스이다.
a = 10
b = "문자열객체"
c = True

print(b.__dir__())  # 문자열 객체 안에 있는 메서드 리스트를 확인가능