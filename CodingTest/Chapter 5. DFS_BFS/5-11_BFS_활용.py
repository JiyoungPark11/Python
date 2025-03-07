# -----------------------------------------------------------------------
# [BFS 활용 예제]미로 탈출
# 주어진 미로에서 (0, 0)에서 (N-1, M-1)까지 가는 최단 거리를 구하는 방식
# 미로에서 1은 이동 가능, 0은 이동 불가능한 벽을 의미
# -----------------------------------------------------------------------

from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 4가지 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append(x, y) # 시작 위치를 큐에 삽입

    while queue: 
        x, y = queue.popleft() # 현 위치 꺼내기
        for i in range(4): # 상하좌우 이동
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m: # 미로 범위를 벗어나면 무시
                continue
            if graph[nx][ny] == 0: # 벽(0)인 경우 무시
                continue
            if graph[nx][ny] == 1: # 방문하지 않은 노드일 경우 최단 거리 업데이트
                graph[nx][ny] = graph[x][y] + 1 # 이전 거리 + 1
                queue.append((nx, ny)) # 큐에 추가하여 계속 탐색
    return graph[n-1][m-1]

print(bfs(0,0))