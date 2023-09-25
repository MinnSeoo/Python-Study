# 보유한 주식이 목표가에 도달했을 때의 종목별 수익금과 수익률을 출력하는 프로그램을 작성해 보자.
# mystock.csv 파일로 부터 종목, 매입가, 수량, 목표가 정보를 가져온다.

# 수익금 = (목표가 - 매입가) * 수량
# 수익률 = (목표가 / 매입가 - 1) * 100

# 문제에서 mystock.csv 파일로 부터 정보를 가져온다고 했으므로
# 사전에 미리 mystock.csv 파일을 생성했다고 가정하겠음.

import csv

def show_profit(data):
    name = data[0]  # 종목
    purchase_price = int(data[1]) # 매입가
    amount = int(data[2])         # 수량
    target_price = int(data[3])   # 목표가

    profit = (target_price - purchase_price) * amount               # 수익금    
    profit_rate = (target_price / purchase_price - 1) * 100         # 수익률
    
    print(f"{name}, {profit}, {profit_rate:.2f}%")          # 수익률은 소수점 둘째 자리에서 반올림 함.
    
# 파일 열기
file = open("./FastCampus/Chap10/mystock.csv", "r", encoding="utf8")

# 파일 데이터 읽기
reader = list(csv.reader(file))

for data in reader[1:]:     # 문자열 슬라이싱 해줌 -> reader[1:] -> 우리는 인덱스의 1부터 2까지의 값만 필요함으로!
    show_profit(data)
    
file.close()


