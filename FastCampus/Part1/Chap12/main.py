import os
import csv
from post import Post

# 파일 경로
file_path = "./FastCampus/Chap12/data.csv"

# post 객체를 저장할 리스트 -> 전역 변수
post_list = []

# file_path에 지정한 경로에 data.csv 파일이 있다면
if os.path.exists(file_path):   
    # 게시글 로딩하기
    print("게시글 로딩중...")
    f = open(file_path, "r", encoding="utf8")   # 파일을 읽기 모드로 연다.
    reader = csv.reader(f)  # csv 파일 읽기
    for data in reader: 
         # post instance 생성하기
        post = Post (int(data[0]), (data[1]), (data[2]), int(data[3]))  # Post 클래스의 인자값들을 차례로 인덱스 번호를 매기고 각 행의 데이터를 사용해 Post 클래스의 인스턴스를 생성
        post_list.append(post)                  

else:       # 없을 경우
    f = open(file_path, "w", encoding="utf8", newline="")   # 파일을 쓰기 모드로 열고 내용을 작성함.
    f.close()
    
    
# print(post_list[0].get_title())     # post_list의 0번째 인덱스에 저장된 title을 출력하라는 뜻.
# print(post_list[0].get_content())   # post_list의 0번째 인덱스에 저장된 content를 출력하라는 뜻.



# 게시글 쓰기
def write_post():
    """ 게시글 쓰기 함수 """
    print("\n\n - 게시글 쓰기 -")
    title = input("제목을 입력해 주세요\n>>> ")     # 제목 입력받기
    content = input("내용을 입력해 주세요\n>>> ")   # 내용 입력받기

    # 글 번호를 받아오기 
    id = post_list[-1].get_id() + 1     # post_list의 마지막 요솟값에 해당하는 값을 가져온후 1을 더해준다. / 게시글을 새로 추가했을 경우 -> 마지막 요소값+1
    post = Post(id, title, content, 0)
    post_list.append(post)  # post_list에 post의 글 번호를 추가해 준다.
    print("~ 게시글이 등록되었습니다. ~")
    
# 게시글 목록을 조회하는 함수
def list_post():        
    """ 게시글 목록 함수 """
    print("\n\n - 게시글 목록 -")
    id_list = []    # 글 번호 담을 리스트
    for post in post_list:
        print("번호 : ", post.get_id())       
        print("제목 : ", post.get_title())         
        print("조회수 : ", post.get_view_count())   
        print("")
        id_list.append(post.get_id())   # id_list에 저장해 list에 있는 글번호 인지 판별하기 위해서.
        
    while True:
        print("Q) 글 번호를 선택해 주세요 (메뉴로 돌아가시려면 -1을 입력해주세요.)")
        try:
            id = int(input(">>> ")) 
            if id in id_list:    
                detail_post(id)
                break
            elif id == -1:
                break
            else:
                print("없는 글 번호 입니다.")
        except ValueError:
            print("숫자를 입력해 주세요.")
             
# 글 상세 page   
def detail_post(id):
    """게시글 상세보기 함수"""
    print("\n\n- 게시글 상세 -")
    
    for post in post_list:
        if post.get_id() == id:
            post.add_view_count()
            print("번호 : ", post.get_id())
            print("제목 : ", post.get_title())
            print("본문 : ", post.get_content())
            print("번호 : ", post.get_view_count())
            target_post = post
            
    while True:
        print("\nQ) 수정 : 1  삭제 : 2 (메뉴로 돌아가려면 -1을 입력)")
        try:
            choice = int(input(">>> "))
            if choice == 1:
                update_post(target_post)
                break
            elif choice == 2:
                delete_post(target_post)
                break
            elif choice == -1:
                break
            else:
                print("\n잘못 입력하였습니다.")
        
        except ValueError:
            print("\n숫자를 입력해 주세요.")
            
# 게시글 수정 
def update_post(target_post):
    """게시글 수정 함수"""
    print("\n\n- 게시글 수정 -")
    title = input("제목을 입력해 주세요\n>>> ")
    content = input("본문을 입력해 주세요\n>>>")
    target_post.set_post(target_post.id, title, content, target_post.view_count)    # id와 view_count는 그대로 사용됨. (자기 자신 그대로 가지고 왔기 때문)
    print("# 게시글이 수정되었습니다.")

# 게시글 삭제
def delete_post(target_post):
    """게시글 삭제 함수"""
    post_list.remove(target_post)
    print(f"제목 : {target_post.title}가 삭제되었습니다.")

# 게시글 저장
def save():
    """게시글 저장 함수"""
    f = open(file_path, "w", encoding="utf8") 
    writer = csv.writer(f)
    for post in post_list:
        row = [post.get_id(), post.get_title(), post.get_content(), post.get_view_count()]  # 각 객체의 정보를 가지고와 row 리스트에 저장
        writer.writerow(row)    # row 리스트에 저장된 정보를 csv 파일의 한 행에 쓴다.
    f.close()
    print("저장이 완료되었습니다.")
    print("# 프로그램 종료!")
        


# 메뉴 출력하기
while True:
    print("\n\n- FCM BLOG - ")
    print("- 메뉴를 선택하세요 -")
    print("1. 게시글 쓰기")
    print("2. 게시글 목록")
    print("3. 프로그램 종료")
    try:
        choice = int(input(">>> "))     
    except ValueError:      # 숫자외 다른 값은 error 처리
        print("숫자를 입력해 주세요.")
         
    else:
        if choice == 1:
            write_post()    # 게시글 쓰기
        elif choice == 2:
            list_post()     # 게시글 목록 조회
        elif choice == 3:
            save()
            break