# ----------------------------------------------------------------------------
# BFS(Breadth-First Search) 예제
# 1. 시작 노드를 큐에 넣고 방문 처리를 한다.
# 2. 큐에서 노드를 하나씩 꺼내면서 해당 노드와 연결된 모든 인접 노드를 방문한다.
# 3. 방문하지 않은 노드는 큐에 추가하고 방문 처리를 한다.
# 4. 큐가 빌 때까지 위 과정을 반복한다.
# ----------------------------------------------------------------------------

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start]) # 큐에 시작 노드 추가
    visited[start] = True # 시작노드를 방문 처리
    while queue: # 큐가 빌 때까지 반복
        v = queue.popleft() #큐에서 하나의 원소를 뽑아 출력
        print(v, end=' ')
        for i in graph[v]: # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
            if not visited[i]: # 방문하지 않은 노드라면
                queue.append(i) # 큐에 추가
                visited[i] = True # 방문 처리


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)