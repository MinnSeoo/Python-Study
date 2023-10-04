unit_info = {
    "probe" : {
        "name" : "프로브",
        "mineral" : "50",
        "gas" : "0",
        "hp" : 20,
        "shield" : 20, 
        "demage" : 5
    },
    
    "zealot" : {
        "name" : "질럿",
        "mineral" : "100",
        "gas" : "0",
        "hp" : 100,
        "shield" : 60, 
        "demage" : 16
    },
    
    "dragoon" : {
        "name" : "드라군",
        "mineral" : "125",
        "gas" : "50",
        "hp" : 100,
        "shield" : 80, 
        "demage" : 26
    }
}

class Unit:
    """
    속성 : 이름, 체력, 방어막, 공격력
    """
    
    def __init__(self, name, hp, shield, demage):
        self.name = name
        self.hp = hp
        self.shield = shield
        self.demage = demage


class Player:
    """
    속성 : 닉네임, 미네랄, 가스, 유닛리스트
    메서드 : 유닛 생산 하기
    """
    
    def __init__(self, nick_name, mineral, gas, unit_list=[]):
        self.nick_name = nick_name
        self.mineral = mineral  
        self.gas = gas
        self.unit_list = unit_list
    
    def produce(self, name, mineral, gas, hp, shield, demage):
        if self.mineral - mineral < 0:
            print("미네랄이 부족합니다.")
        elif self.gas - gas < 0:
            print("가스가 부족합니다.")
        else:
            self.mineral -= mineral
            self.gas -= gas
            unit = Unit(name, hp, shield, demage) 
            self.unit_list.append(unit)
            print(f"[{name}]을(를) 생산합니다.")
            

player1 = Player("Bisu", 400, 50)

player1.produce(unit_info['probe']['name'], int(unit_info['probe']['mineral']), int(unit_info['probe']['gas']),
                int(unit_info['probe']['hp']), int(unit_info['probe']['shield']), int(unit_info['probe']['demage']))
        
player1.produce(unit_info['zealot']['name'], int(unit_info['zealot']['mineral']), int(unit_info['zealot']['gas']),
                int(unit_info['zealot']['hp']), int(unit_info['zealot']['shield']), int(unit_info['zealot']['demage']))

player1.produce(unit_info['dragoon']['name'], int(unit_info['dragoon']['mineral']), int(unit_info['dragoon']['gas']),
                int(unit_info['dragoon']['hp']), int(unit_info['dragoon']['shield']), int(unit_info['dragoon']['demage']))
         
         
# 생성된 모든 유닛을 확인
for unit in player1.unit_list:
    print(f"[{unit.name}]  체력 : {unit.hp},  방어막 : {unit.shield},  공격력 : {unit.demage}")