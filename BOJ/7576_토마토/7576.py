from collections import deque
import sys

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

# 제너레이터 사용 list에서 target 찾는 함수
def find(myList: list, target=1):
    for idx in range(len(myList)):
        if myList[idx] == target:
            yield idx

def solution():
    global box, N, M, q

    M, N = map(int, sys.stdin.readline().split())
    box = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    # 이미 익은 토마토들을 찾아서 큐에 넣어줌
    q = deque()
    for i in range(N):
        for j in find(box[i]):
            q.append((i, j))

    # BFS
    last_location = (N, M) # BFS에서 마지막으로 큐에 넣은 좌표(마지막으로 익은 토마토 좌표)
    while (q):
        row, col = q.popleft()
        for i in range(4):
            n_row, n_col = (row+dy[i], col+dx[i])

            if (0 <= n_row < N and 0 <= n_col < M and box[n_row][n_col] == 0):
                box[n_row][n_col] = box[row][col] + 1
                q.append((n_row, n_col))
                last_location = (n_row, n_col)

    # 안 익은 토마토가 있는지 확인
    isnotriped = any(0 in line for line in box)

    # 안 익은 토마토가 있는 경우
    if (isnotriped):
        days = -1
    # 최종 좌표가 (N, M)이면 루프 한 번도 안 돌았다는 뜻이므로, 이미 토마도가 모두 익은 상태
    elif (last_location == (N, M)):
        days = 0
    # 나머지 경우 최종 좌표값-1 이 익는 데 소요되는 날짜임
    else:
        days = box[last_location[0]][last_location[1]] - 1

    print(days)

solution()
