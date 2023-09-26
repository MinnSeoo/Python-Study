# 리스트 내포란? -> for, if문을 지정하여 리스트를 간편하게 만드는 것.
# [ 순서 ]
# for -> if -> 표현식 -> 리스트

# for문 사용!
nums = [i for i in range(5)]
print(nums)

nums2 = [100, 200, 300, 400, 500]
double_num2 = [i * 2 for i in nums2]
print(double_num2)

# if문 사용!
nums3 = [i for i in range(10) if i % 2 == 0]    # ->  i의 범위 0~9 중에 2로 나눈 나머지가 없는 정수만 표현식 i에 저장됨.
print(nums3)    # 출력시 [ 0,2,4,6,8 ]

nums4 = [10,20,30,40,50]
double_num3 = [i * 2 for i in nums4 if i >=40 ]
print(double_num3)

