import sqlite3  # 모듈 추가

# DB 열기
conn = sqlite3.connect("Chap5/test-sql.db")

# 커서 생성 
cur = conn.cursor()

# sql 명령어 작성
INSERT_SQL = """ INSERT INTO drink(company, name, price); 
                 VALUSE (?, ?, ?)"""        # 순차적으로 데이터가 들어감.

# sql 명령 실행 
cur.execute(INSERT_SQL, ("롯데", "칠성 사이다", "1200"))

# 데이터 한번에 여러개 추가하기
data = [
    ["korea coca cola", "coca cola zero", "1500"]
    ["pepsiCo", "pepsi cola zero", "1500"]
]

cur.executemany(data) # -> 여러개의 값을 받아오기 때문에 excutemany 사용하기!


# INSERT, UPDATE, DELETE -> 반드시 commit 하여 저장해야함!
conn.commit()

# db 닫기
conn.close()