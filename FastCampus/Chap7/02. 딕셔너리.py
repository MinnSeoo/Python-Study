# 딕서녀리 란? -> 사전형태의 자료형
#             -> key 와 value를 1 대 1로 대응시킨 형태 

# 딕셔너리 만들기
stock_a = {"삼성전자" : 85000, "LG 전자" : 98000}

stock_b = {
    "삼성전자" : [80000, 10000, 110000, 120000],
    "카카오" : [10000, 20000, 50000, 3000]
}

stock_c = {
    "삼성전자" : {
        "현재가" : 82000,
        "보유수량" : 3,
        "매수단가" : 81000
    }
}

print(stock_a)
print(stock_b)
print(stock_c)

# 딕셔너리 접근하기
print(stock_a["삼성전자"])  # 딕셔너리에 key 값을 넣어주면 해당하는 key 값에 대한 데이터가 출력된다.
print(stock_b["카카오"])
print(stock_c["삼성전자"]["매수단가"])  # 중첩된 딕셔너리의 키 값 출력

# 딕셔너리 할당하기
stock_a["삼성전자"] = 100
print(stock_a)


# 딕셔너리 삭제하기
del stock_a["LG 전자"]  # del 함수를 통해서 딕셔너리의 값을 삭제할 수 있다.
print(stock_a)


# 딕셔너리 함수
stock_dic ={
    "삼성전자" : 1,
    "SK 전자" : 200,
    "카카오" : 300,
    "네이버" : 400
}


# items() -> key와 데이터를 한 쌍으로 나타냄 ex) "과일" : 사과
for item in stock_dic.items() :
    print(item)

# keys() -> key 값만 출력
for key in stock_dic.keys():
    print(key)

# values() -> data 값만 출력
for value in stock_dic.values():
    print(value)