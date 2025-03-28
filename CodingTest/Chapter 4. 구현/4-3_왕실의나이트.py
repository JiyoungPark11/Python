# --------------------------------------------------------------------------------
# 8 * 8 체스판이 존재할 때, 특정 위치에 있는 나이트가 이동할 수 있는 경우의 수 구하기
# 나이트는 L자로만 이동 가능하고 다음과 같은 2가지 경우로 이동할 수 있다
# 1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
# 2. 수직으로 두칸 이동한 위에 수평으로 한 칸 이동하기 
# --------------------------------------------------------------------------------
# ord() = 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수 반환
# --------------------------------------------------------------------------------

# 현재 나이트의 위치 입력 받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a') + 1)

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, -2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능하지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)