# 높이 stair인 계단을, possible_steps 배열에 있는 만큼 한 번에 오를 수 있다.
# 오르는 방법의 수를 리턴한다
def staircase(stairs, possible_steps):
    # 여기에 코드를 작성하세요

    way_by_height = [1, 1]  # 계단높이가 0,1 이면 방법은 1개씩임

    for i in range(2, stairs + 1):  # 계단높이가 2일때 부터 stair까지
        way_by_height.append(0)  # 배열에 i번째 계단 추가

        for j in possible_steps:  # 하나씩 가능성 검토
            if i - j >= 0:  # 음수가 아니면
                way_by_height[i] += way_by_height[i - j]  # 더함
                # 즉 첫번째 케이스에서 5번째 계단 가려면, 4or3or2에서 가니까!
    return way_by_height[stairs]


print(staircase(5, [1, 2, 3]))
print(staircase(6, [1, 2, 3]))
print(staircase(7, [1, 2, 4]))
print(staircase(8, [1, 3, 5]))