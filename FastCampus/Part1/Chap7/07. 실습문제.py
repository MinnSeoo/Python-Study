# 실습 문제 풀이

class iteam:
    def __init__(self, name, price, weight, isdropable):
        self.name = name
        self.price = price
        self.weight = weight
        self.isdropable = isdropable
    
    def sale(self): # 판매
        print(f"[{self.name}] 판매가격은 [{self.price}]")
    
    def discard(self):  # 버리기
        if self.isdropable:
            print(f"[{self.name}] 버렸습니다.")
        else:
            print(f"[{self.name}] 버릴 수 없습니다.")
            
    
class WearableItem(iteam):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect    # 효과
    
    def wear(self): # 착용하기 메소드
        print(f"[{self.name}]을 착용했습니다. {self.effect}")
    
    
class UsableItem(iteam):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect # 사용효과
    def use(self):  # 사용하기
        print(f"[{self.name}] 사용했습니다. {self.effect}")


# 인스턴스 생성
sword = WearableItem("닌자검", 20000, 2.5, True, "체력 : 500 증가") 
sword.wear()    # WearableItem 클래스는 iteam 클래스를 상속받은것이기 때문에 iteam 메소드를 사용할 수 있다.
sword.sale()
sword.discard()

potion = UsableItem("잠이 안온다? 물약", 1000, 0.5, False, "구라다. 헹 속앗지? ㅋ")
potion.use()
potion.sale()
potion.discard()
        