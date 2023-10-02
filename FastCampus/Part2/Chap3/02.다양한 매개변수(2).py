# 1. 위치 가변 매개변수
# 가변 매개변수 -> 개수가 정해지지 않은 매개변수
# 매개변수 앞에 * 가 붙는다 -> 튜플형

def print_fruits(*args):
    for arg in args:
        print(arg)
        
print_fruits('apple', 'pinapple', 'peach', 'grape')


# 2. 키워드 가변 매개변수
# 매개변수 앞에 ** 가 붙는다 -> 딕셔너리형

def comment_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
        
comment_info(name = '파린이', content = '알려주셔서 감사합니다!')



# 매개변수 작성 순서
# 위치 - 기본 - 위치 가변 - 키워드(기본) - 키워드 가변
def post_info(title, content, *tags):
    print(f"제목 : {title}")
    print(f"내용 :{content}")
    print(f"태그 : {tags}")
    
post_info('매개변수 작성 순서에 대하여 알아보자', '매개변수 작성 순서란 ...', '#Python')

# 그럼 만약 위치 가변 매개변수가 위치, 기본 매개변수 보다 앞에 작성되어 있으면 어떤 일이 발생할까?
def post_info2(*tags, title, content):
    print(f"제목 : {title}")
    print(f"내용 : {content}")
    print(f"태그 : {tags}")
    
post_info2('# Python','# 파이썬', '매개변수 작성 순서에 대하여 알아보자', '매개변수 작성 순서란 ...')

# 이 경우엔 오류가 발생한다. 
# 왜냐하면 위치 가변 매개변수는 어려개의 인자값을 받을 수 있기 때문이다.
# 위 코드느 위치 매개변수가 tags, title, content의 갑까지 인자로 받아오기 때문에 title, content에 넘겨줘야할 인자값이 없기 때문에 오류가 발생한다.
    