from collections import deque
import sys


def dfs(v, visited):
    visited[v] = 1
    print(v, end=" ")
    for i in range(1, N+1):
        if (not visited[i] and matrix[i][v]):
            dfs(i, visited)


def bfs(v, visited):
    q = deque()
    q.append(v)
    visited[v] = 1
    while (q):
        v = q.popleft()
        print(v, end=" ")
        for i in range(1, N+1):
            if (not visited[i] and matrix[i][v]):
                q.append(i)
                visited[i] = 1


def solution():
    global N, M, matrix
    N, M, V = map(int, sys.stdin.readline().split())

    # 인접행렬 초기화
    matrix = [[0]*(N+1) for _ in range(N+1)]

    # 인접행렬에 간선 추가
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        matrix[a][b] = matrix[b][a] = 1

    # visited 배열 초기화
    visited = [0]*(N+1)

    dfs(V, visited[:])
    print()
    bfs(V, visited)

solution()
