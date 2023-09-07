import os
import csv
from post import Post

# 파일 경로
file_path = "./FastCampus/Chap12/data.csv"

# post 객체를 저장할 리스트
post_list = []

# data.csv 파일이 있다면
if os.path.exists(file_path):
    # 게시글 로딩하기
    print("게시글 로딩중...")
    f = open(file_path, "r", encoding="utf8")
    reader = csv.reader(f)
    for data in reader:
         # post instance 생성하기
        post = Post (int(data[0]), (data[1]), (data[2]), int(data[3]))  
        post_list.append(post)                  

else:
    f = open(file_path, "w", encoding="utf8", newline="")   # 파일 생성
    f.close()
    
    
print(post_list[0].get_title())     # post_list에 저장된 title을 출력하라는 뜻.
print(post_list[0].get_content())