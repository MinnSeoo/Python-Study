# 예외처리가 필요한 이유
# -> 프로그램 실행중에 발생하는 에러를 미연에 방지하기 위함.

# 예외처리 연습!
# 원화를 입력, 환율 입력 -> 달러값

won = input("원화금액을 입력하세요 : ")
dollar = input("환율을 입력하세요 : ")

try:    # 예외가 발생할 수 있는 코드
    print(int(won) / int(dollar))
except ValueError as e: # 예외가 발생했을 때 실행되는 코드
    print(f"{e}\n문자열 예외가 발생했습니다.")
except ZeroDivisionError as e:
    print(f"{e}나누기 0은 불가능 합니다.")
else:
    print("예외가 발생하지 않았습니다. ")
finally:
    print("예외 발생 여부에 상관없이 항상 실행됩니다.")