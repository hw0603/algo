from collections import deque
import sys


def bfs(V):
    q = deque([V])
    while (q):
        x = q.popleft()
        if (x == K):
            return dist[x]
        for nx in (x-1, x+1, x*2):
            if (0 <= nx <= MAX and not dist[nx]):
                dist[nx] = dist[x] + 1
                q.append(nx)
    return -1

def solution():
    global MAX, dist, N, K
    MAX = 10 ** 5
    dist = [0] * (MAX + 1)
    N, K = map(int, sys.stdin.readline().split())

    print(bfs(N))

solution()
