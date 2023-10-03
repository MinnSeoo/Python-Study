# 상속이란 ?
# -> 클래스들의 공통된 속성과 메서드를 뽑아내서 부모 클래스를 만듬
# -> 이를 자식 클래스에서 상속받아서 사용함.

# 상속의 장점!
# -> 코드의 중복을 제거할 수 있다.
# -> 유지보수가 편리해 진다.


class Item:
    """
    속성 : 이름
    메서드 : 줍기, 버리기
    """
    
    def __init__(self, name):
        self.name = name
        
    def pick(self):
        print(f"[{self.name}]을(를) 주웠습니다.")
        
    def discard(self):
        print(f"[{self.name}]을(를) 버렸습니다.")
        
        
class Weapon(Item):
    """
    속성 : 공격력
    메서드 : 공격하기
    """
    
    def __init__(self, name, demage):
        super().__init__(name)  # 부모클래스를 호출 하고 생성자를 호출해 name을 넘겨줌.
        self.demage = demage
        
    def attack(self):
        print(f"[{self.name}]을(를) 이용해 {self.demage}로 공격합니다.")


class HealingItem(Item):
    """
    속성 : 회복량 
    메서드 : 사용하기
    """
    
    def __init__(self, name, recovery_amount):
        super().__init__(name)
        self.recovery_amount = recovery_amount
        
    
    def use(self):
        print(f"[{self.name}]을(를) 사용해서 {self.recovery_amount} 만큼 회복합니다.")
        

m16 = Weapon("m16", 100)
bungdae = HealingItem("붕대", 20)

m16.attack()
bungdae.use()