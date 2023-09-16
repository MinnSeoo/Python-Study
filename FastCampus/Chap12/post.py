# main.py의 모듈로 사용된다.

# get : 속성값을 가지고 올때 주로 사용됨.
# set : 속성값을 변경할때 주로 사용됨.


# 필요한 기능? 들?
# 글번호, 글제목, 글내용, 조회수
#

class Post:         # docstring을 사용해 메소드에 대한 설명을 기재함.
    """         
        게시물 클래스
        param id: 글번호
        param title: 글제목
        param content: 글내용 
        param view_count: 조회수
    """
    
    # 생성자
    def __init__(self, id, title, content, view_count):
        self.id = id                    # 게시물 리스트 id
        self.title = title              # 게시물의 제목
        self.content = content          # 게시물 내용 
        self.view_count = view_count    # 게시물 조회수
        
    # 게시물 수정
    def set_post(self, id, title, content, view_count):
        self.id = id
        self.title = title
        self.content = content
        self.view_count = view_count
     
    # 조회수 증가 메서드    
    def add_view_count(self):
        self.view_count += 1    # 게시물을 조회시 1증가
        
    # 게시물 목록, 상세보기에 활용될 메서드
    def get_id(self):
        return self.id  
    
    # 게시물 제목
    def get_title(self):
        return self.title
    
    # 게시물 내용
    def get_content(self):
        return self.content
    
    # 조회수
    def get_view_count(self):
        return self.view_count
    

if __name__ == "__main__":
    post = Post(1, "테스트", "테스트입니다.", 0)
    # post.set_post(1, "데스트2", "테스트2입니다", 0)
    post.add_view_count()   # -> cnt + 1
    print(f"{post.get_id()} {post.get_title()} {post.get_content()} {post.get_view_count()}")
    