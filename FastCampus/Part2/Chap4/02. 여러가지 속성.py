# 인스턴스 속성 
# -> 객체마다 다르게 가지는 속성

# 클래스 속성
# -> 모든 객체가 공유하는 속성

# 비공개 속성 (private)
# -> 클래스 안에서만 접근 가능한 속성

# ------------------------------------------------------------------
class Unit:
    """인스턴스 속성 : 이름, 체력, 방어막, 공격력
    """
    count = 0

    def __init__(self, name, hp, shield, demage):
         self.name = name  
         self.__hp = hp         # private 속성
         self.shield = shield
         self.demage = demage
         Unit.count += 1 
         print(f"[{self.name}](이)가 생성 되었습니다.")

    def __str__(self):
        return f"[{self.name}] 체력 : {self.__hp},  방어막 : {self.shield},  공격력 : {self.demage}"

probe = Unit("프로브", 20, 20, 5)

zealot = Unit("질럿", 100, 50, 10)

dragoon = Unit("드라군", 100, 80, 30)

print(probe)
print(zealot)
print(dragoon)

# 인스턴스 속성 수정 -> 클래스 밖에서 속성을 사용하려면 "객체명.속성" 이런식으로 작성해 줘야한다.
probe.demage += 1
print(probe)

# 비공개 속성 접근
probe.__hp = 9999
print(probe)    # 값이 바뀌지 않음! 

# 그럼 비공개 속성에 아예 접근이 불가한가? -> x (그건 아니다)
# 네임 맹글링 (name mangling) 이라는 방법을 통해 접근 가능하다 (이름을 바꾸는 기술을 사용해 접근이 조금 어렵도록 만들어둔 방법이다.)
probe._Unit__hp = 9999
print(probe)

# 전체 유닛 개수를 출력
print(Unit.count)