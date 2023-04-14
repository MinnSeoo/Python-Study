# for 문 
# Case1 - 리스트 사용
champions = ["티모", "리신", "모르가나", "쟈크"]

for champion in champions:
    print("선택한 챔피언은",champion, "입니다.")


# Case2 - 문자열 사용
fighting_message = " 힘들어도 포기하지 말자!"

for word in fighting_message:
    print(word)
    

# Case3 - range 객체 사용
# range 함수는 range(시작, 끝+1)
# [조건] - 0~9 까지 숫자를 포함하는 range 객체 출력

for i in range(10):
    print(i)


# range 함수는 총 3개의 인자를 받을 수 있음 
# ex) 
for i in range(1,9,3):
    print(i) 

