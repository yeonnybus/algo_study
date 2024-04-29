

#(N + 1)의 크기인 리스트에, 1부터 N까지의 임의의 자연수가 요소로 할당되어 있음.
#-> 적어도 하나의 수는 중복될 것! 비둘기집의 원리 같음.
#반복되는 수를 찾아내야함.

#단, O(n) 이상의 공간 사용할 수 없으며 인풋으로 받는 리스트를 변형할 수 없음

def find_same_number(some_list):

    length = len(some_list)
    start = 1
    end = length - 1

    while start < end:
        mid = (start + end) // 2
        a = 0
        b = 0

        for i in some_list:
            if i > mid and i <= end:
                b += 1
            elif i <= mid and i >= start:
                a += 1
        
        if a > b:
            end = mid
        else:
            start = mid+1

    return start


# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))