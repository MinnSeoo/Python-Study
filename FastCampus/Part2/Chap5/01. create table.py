import sqlite3  # 모듈 추가

# DB 열기
conn = sqlite3.connect("Chap5/test-sql.db")

# 커서 생성 
cur = conn.cursor()

# sql 명령어 작성
CREATE_SQL = """
    CREATE TABLE IF NOT EXISTS Items(
        id integer primary key autoincrement,
        company text not null,
        name text not null, 
        price text not null
        
    );


"""


# sql 명령 실행 
cur.execute(CREATE_SQL)


# db 닫기
conn.close()