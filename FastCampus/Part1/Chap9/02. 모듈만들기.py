import pay_moudule
# import reservation

# 변수사용
print(pay_moudule.version)

# 함수 사용 
pay_moudule.printAuthor()

# 클래스 사용
pay_info = pay_moudule.Pay("A1231","10000","2023-09-01")
print(pay_info.get_pay_info())


if __name__ == "__main__": 
    print(pay_moudule.__name__)     # main 페이지인 모듈이 아닌 다른 파일에서 실행했을 경우 main 페이지의 파일명을 출력한다.
    

# TEST!
# 변수
# print(reservation.region)

# reservation.theater()

# a = reservation.theater("minseo", "010-1111-2222", "CGV")
# print(reservation.get_reservation())

