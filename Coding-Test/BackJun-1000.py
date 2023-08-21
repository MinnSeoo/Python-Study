class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result
    
    def mul(self):
        result = self.first - self.second
        return result


    def sub(self):
        result = self.first * self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result

a = FourCal(10,2)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())

# 클래스 상속
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

# 메서드 오버라이딩
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
           return self.first / self.second

a = MoreFourCal(4,2)
print(a.pow())

a = SafeFourCal(5,0)
print(a.div)

# 클래스 변수
class MyName:
    name = 'minseo'

n1 = MyName()
n2 = MyName()
print(n1.name)
print(n2.name)

n1.name = 'Jung-Min-Seo'

print(n1.name)
print(n2.name)


