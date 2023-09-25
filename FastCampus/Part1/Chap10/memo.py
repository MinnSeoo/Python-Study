# 게시물의 총 개수와 한 페이지에 보여 줄 게시물의 수를 입력으로 주어졌울 때 총 페이지 수를 출력하는 프로그래밍을 구현하여라.
# ex) 현재 총 10개의 게시물이 있다. 한 페이지에는 최대 2개의 게시물을 보여줄 수 있다. 이때 게시판의 총 페이지 수는?
# an) 10개의 게시물, 한 페이지당 최대 2개의 게시물 전시 가능 -> 총 5페이지

# 공식 -> 총 페이지 수 = (총 게시물 수 / 한 페이지당 보여줄 개수) + 1 
# 위에서 +1을 하는 이유는 수가 나누어 떨어지지 않을 경우도 생각해서
# 총 페이지 수 = (27 / 5) + 1  
# -> 6장 

# 함수명 : notice
# 총 페이지 수 : result
# 총 게시물 수 : m
# 한 페이지당 보여줄 개수 : n


def notice(m,n):
    page= 0
    if int(m) % int(n) !=0:
        page = int(m) // int(n) + 1
        return page
    else:
        page = int(m) // int(n)
        return page
    

m = input("총 게시물 수를 입력하세요 : ")
n = input("한 페이지 당 보여줄 게시물 수를 입력하세요 : ")
result = notice(m,n)

print(f"총 페이지 수는 : {result} 페이지 입니다.")


# 다시한번 복습 해 보자!
# m = 게시물의 총 개수
# n = 페이지당 보여줄 게시물 수

def total_page(m,n):
    if m % n == 0:
        return m // n
    else:
        return (m // n) + 1
    
print(total_page(10,1))
print(total_page(5,3))
print(total_page(8,10))
print(total_page(9,10))