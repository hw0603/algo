from collections import deque
import sys

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, area):
    q.append([x, y])
    matrix[x][y] = area
    while (q):
        x, y = q.popleft()
        # 4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < N and 0 <= ny < M):
                if (matrix[nx][ny] == 0):
                    matrix[nx][ny] = area # 영역 번호 할당
                    q.append([nx, ny])

def solution():
    # 0: 방문 안 함, 1~X: 영역 번호, -1: 직사각형 영역
    global q, matrix, N, M

    M, N, K = map(int, sys.stdin.readline().split())
    matrix = [[0]*M for _ in range(N)]
    q = deque()

    # 직사각형 범위 설정
    for _ in range(K):
        x1, y1, x2, y2 = map(int, input().split())
        for i in range(x1, x2):
            for j in range(y1, y2):
                matrix[i][j] = -1

    area = 1 # 영역 번호
    for i in range(N):
        for j in range(M):
            if (matrix[i][j] == 0):
                bfs(i, j, area)
                area += 1

    area -= 1 # 1부터 시작했으므로 하나 빼줌
    print(area)
    # 각 영역의 넓이 구함
    size_list = [0] * area
    for i in range(N):
        for j in range(M):
            if (matrix[i][j] > 0):
                size_list[matrix[i][j]-1] += 1
    size_list.sort()
    for size in size_list:
        print(size, end=" ")



solution()
