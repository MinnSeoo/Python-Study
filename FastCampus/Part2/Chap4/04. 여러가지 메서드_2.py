# 정적 메서드 
# 객체를 생성할 필요없이 바로 호출 가능하다!
class Math:
    @staticmethod
    def add(x,y):
        return x + y
    
    @staticmethod
    def sub(x,y):
        return x - y
    
print(Math.add(10,5))
print(Math.sub(10,5))