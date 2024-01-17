# 이터레이터 생성방법

# 4가지의 계절이 순서대로 담겨져있는 이터레이터를 생성
class Seasons:
    def __init__(self):
        self.season_list = ['spring', 'summer', 'fall', 'winter']
        self.idx = 0
        self.max_num = 4
        
    def __iter__(self):     # 이터 객체 호출시 객체 자기 자신을 반환 
        return self
        
    def __next__(self):
        if self.idx < self.max_num:     # idx가 max_num 보다 작을동안 -> season_list의 인덱스 길이만큼 실행됨
            current_idx = self.idx      # current_idx에 현재 idx 값을 저장
            self.idx += 1               # idx를 1 증가후 
            return self.season_list[current_idx]        # season_list의 current_idx에 위치한 요소 값 출력 
        else:
            raise StopIteration         # season_list를 다 출력후 종료 -> 이 코드는 굳이 안써도됨 (next 메서드가  종료후 자동으로 호출되기 때문!)
            

# for i in Seasons():
#     print(i)
        
iter_obj = Seasons().__iter__()

print(iter_obj.__next__())
print(iter_obj.__next__())
print(iter_obj.__next__())
print(iter_obj.__next__())
# print(iter_obj.__next__())        # -> stopIteration 발생!
