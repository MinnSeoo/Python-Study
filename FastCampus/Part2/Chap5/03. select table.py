import sqlite3  # 모듈 추가

# DB 열기
conn = sqlite3.connect("Chap5/test-sql.db")

# 커서 생성 
cur = conn.cursor()

# sql 명령어 작성
SELECT_SQL = "SELECT * FROM item;"

# sql 명령 실행 
cur.execute(SELECT_SQL)

rows = cur.fetchall()
for row in rows:
   print(row) 

# db 닫기
conn.close()