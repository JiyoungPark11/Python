# N * N 정사각형 공간 위에 서있다고 가정
# N * N  크기의 정사각형 공간을 벗어나는 움직임은 무시됨
# 목표 : 이동 계획서가 주어졌을 때, 여행가 A가 최종적으로 도착할 지점의 좌표를 출력
# -----------------------------------------------------------------------------
print("N을 입력하세요: ")
n = int(input())
x, y = 1, 1
print("이동계획을 입력하세요: ")
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_type)):
        if plan == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)
