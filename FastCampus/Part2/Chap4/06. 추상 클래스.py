# 추상클래스를 사용하기 위해선 abc 모듈을 가지고 와야함
from abc import *

# 추상 클래스를 생성하면 추상 메서드를 사용할 수 있다
# -> @abstractmethod 라는 데코레이터를 작성하면 추상메소드를 뜻한다
# -> 부모 클래스에서 추상 메소드를 구현하면 상속받는 자식 클래스에서 구현을 해야 한다.
# -> 그렇지 않을 경우 오류가 발생한다.

class Item(metaclass=ABCMeta):  # 추상클래스
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
        
    @abstractmethod
    def use(self):
        pass
        
        
class Weapon(Item):
    """
    속성 : 공격력
    메서드 : 공격하기
    """
    
    def __init__(self, name, demage):
        super().__init__(name)  # 부모클래스를 호출 하고 생성자를 호출해 name을 넘겨줌.
        self.demage = demage
        
    def use(self):
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

m16.use()
bungdae.use()