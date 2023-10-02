# 실습 문제 1
# 변경 전 - ['apple', 'watch', 'apolo', 'star', 'abocado']
# 변경 후 - ['apple', 'apolo', 'abocado']

# 1. 리스트 내포를 사용하지 않은 경우.
word_list = ['apple', 'watch', 'apolo', 'star', 'abocado']
new_word_list = []
for word in word_list:
    if word[0] == 'a':
        new_word_list.append(word)



# 2. 리스트 내포를 사용
word_list = ['apple', 'watch', 'apolo', 'star', 'abocado']
new_word_list = [word for word in word_list if word[0] == 'a']
print(new_word_list)


# ------------------------------------------------------------------

# 실습 문제 2
# 변경 전  - ['오메가3', None, '비타민C500', None, '홍삼절편']
# 변경 후 - ['오메가3', '', '비타민C500', '', '홍삼절편']

items = ['오메가3', None, '비타민C500', None, '홍삼절편']

# 1. 리스트 내포 사용 전
result = []
for item in items:
    if item != None:
        result.append(item)
    else:
        result.append('')
print(result)
        

# 2. 리스트 내포를 사용 후
result2 = [i if i != None else '' for i in items]    # else문도 포함시키고 싶으면 for 문 앞에 작성해야함!
print(result2)

        

