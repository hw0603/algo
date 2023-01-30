from collections import deque
import sys

def BFS(water, swan, W, H, lake):
    pos = {(0, 1), (0, -1), (-1, 0), (1, 0)}

    # 기준점이 될 백조 한마리의 좌표 언팩
    endX, endY = swan.pop()

    days = 1
    while (swan):
        temp = deque()
        while (water):
            x, y = water.popleft()
            # 물의 좌표를 하나씩 pop 하면서 4방향 탐색
            for p in pos:
                nx = x + p[0]
                ny = y + p[1]
                # lake의 범위 안에 있을 때
                if (0 <= nx < H and 0 <= ny < W):
                    # 그 좌표가 빙하면 물로 바꿔줌
                    if lake[nx][ny] == 'X':
                        lake[nx][ny] = '.'
                        temp.append((nx, ny))
        # 하루가 지나 추가된 물의 좌표 업데이트
        water = temp

        temp = deque()
        # 모든 백조가 있을 수 있는 좌표를 확인할 때 까지 반복
        while (swan):
            # 다른 백조의 좌표 언팩
            x, y = swan.popleft()

            # 두 백조가 만나서 좌표값이 같아지면 days 반환
            if (x == endX and y == endY):
                return days

            # 백조의 좌표로부터 4방향 탐색
            for p in pos:
                nx = x + p[0]
                ny = y + p[1]

                # 그 방향이 lake의 범위에 있을 때
                if (0 <= nx < H and 0 <= ny < W):
                    # 탐색한 좌표가 물이거나 백조라면(백조가 갈 수 있는 좌표 중 아직 확인하지 않은 좌표라면) 값을 days로 바꿔준 후 그 좌표를 swan에 추가
                    if (lake[nx][ny] == '.' or lake[nx][ny] == 'L'):
                        lake[nx][ny] = days
                        swan.append((nx, ny))
                        temp.append((nx, ny))
        # -> 더 이상 갈 수 있는 곳이 없는데 아직 못 만나서 루프 탈출한 경우 temp에 쌓여있는 좌표들을 swan으로 복구
        swan = temp
        days += 1

    return -1

def solution():
    lake = []
    water = deque()
    swan = deque()
    H, W = map(int, sys.stdin.readline().split())

    for _ in range(H):
        lake.append(list(str(sys.stdin.readline().strip())))

    for i in range(H):
        for j in range(W):
            if lake[i][j] == "L":
                swan.append((i, j))
                water.append((i, j))
            elif lake[i][j] == ".":
                water.append((i, j))

    print(BFS(water, swan, W, H, lake))


solution()
