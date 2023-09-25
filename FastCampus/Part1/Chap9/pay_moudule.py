# 결제 정보, 관리 모듈
# 변수
version = 2.0

# 함수
def printAuthor():
    print("작성자는 ?")

# 클래스
class Pay:
    def __init__(self, id, price, time):
        self.id = id
        self.price = price
        self.time = time
        
    def get_pay_info(self):
        return f"{self.id, self.price, self.time}"
        
if __name__ == "__main__":  # 이 코드는 해당 파일을 직접 실행했을 경우에만 생성된다. 
    print(__name__)
    

# TEST
# 영화좌석 예매 모듈 생성
# 지역은 광주로 고정
region = "광주광역시"

# 함수
def theater(user):
    if user == "CGV":
        print("CGV를 선택하셨습니다.")
    elif user == "롯데시내마":
        print("롯데시내마를 선택하셨습니다.")
    elif user == "메가박스":
        print("메가박스를 선택하셨습니다.")
    else:
        print("다시 입력해 주세요.")


class reservation:
    def __init__(self, name, phone, movie):
        self.name = name
        self.phone = phone
        self.movie = movie
    
    def get_reservation(self):
        return f"{self.name, self.phone, self.movie}"
        
