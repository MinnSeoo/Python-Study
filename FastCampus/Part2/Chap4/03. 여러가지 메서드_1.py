# 인스턴스 메서드 
# -> 인스턴스 속성에 접근할 수 있는 메서드.
# -> 항상 첫번째 파라미터로 self를 갖는다.

# 클래스 메서드
# -> 클래스 속성에 접근하기 위해 사용한다.
# 클래스를 의미하는 cls를 파라미터로 받는다.
# @classmethod -> 데코레이터를 작성해 줘야함.

# 정적 메서드
# -> 인스턴스를 만들 필요가 없는 메서드
# -> self를 받지 않는다
# -> 메서드가 인스턴스 유무와 관계없이 독립적으로 사용될 때
# @staticmethod 작성해 줘야함.

# 매직 메서드
# 클래스안에 정의할 수 있는 스페셜 메서드
# 특별한 상황에 호출된다.
# __이름__ 의 형태로 되어있다.

class Unit:
    """인스턴스 속성 : 이름, 체력, 방어막, 공격력
    """
    count = 0

    def __init__(self, name, hp, shield, demage):       # 매직 메서드
         self.name = name  
         self.hp = hp
         self.shield = shield
         self.demage = demage
         Unit.count += 1 
         print(f"[{self.name}](이)가 생성 되었습니다.")

    def __str__(self):      # 매직 메서드
        return f"[{self.name}] 체력 : {self.hp},  방어막 : {self.shield},  공격력 : {self.demage}"

    # 인스턴스 메서드 (instance method) -> 인스턴스 :  메모리 상에 객체가 실체해 있다. 라는 뜻
    def hit(self, demage):
        # 방어막 변경
        if self.shield >= demage:
            self.shield -= demage
            demage = 0
        else:
            demage -= self.shield
            self.shield = 0
            
        # 체력 변경 
        if demage > 0:
            if self.hp > demage:
                self.hp -= demage
            else:
                self.hp = 0
        
        
    # 클래스 메서드 (class method)
    @classmethod
    def print_count(cls):
        print(f"생성된 유닛 개수 : [{cls.count}]개")
        
    
probe = Unit("프로브", 20, 20, 5)

zealot = Unit("질럿", 100, 50, 10)

dragoon = Unit("드라군", 100, 80, 30)

for i in range(1,4):
    probe.hit(16)
    print(probe)
    
Unit.print_count()

print(dir(probe))