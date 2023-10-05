import sqlite3  # 모듈 추가

# DB 열기
conn = sqlite3.connect("Chap5/test-sql.db")

# 커서 생성 
cur = conn.cursor()

# sql 명령어 작성
UPDATE_SQL = "UPDATE Items set price = 1500;"

cur.execute(UPDATE_SQL)

# db 닫기
conn.close()