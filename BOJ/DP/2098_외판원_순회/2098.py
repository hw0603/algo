import sys

N = int(sys.stdin.readline())  # 도시 개수
cities = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 비용 행렬

# N개의 비트 모두 ON
VISITED_ALL = (1 << N) - 1

# DP를 위한 캐시 초기화
# 도시의 개수(N)에 대응하고 (1 << N)을 통해 방문한 도시 집합(visited)에 대응
# dp[N][visited] : N번 -> visited에서 방문 X한 도시 -> 0번 도시(시작 도시) 경로 저장한다고 생각하면 쉬움
dp = [[None] * (1 << N) for _ in range(N)]
choose = [[None] * (1 << N) for _ in range(N)]


def TSP(last, visited) -> int:
    # 마지막 도시 -> 0번째 도시 사이에 경로 존재 시 경로값 반환
    if (visited == VISITED_ALL):
        dp[last][visited] = cities[last][0]
        return cities[last][0] if cities[last][0] > 0 else sys.maxsize  # 마지막 도시 -> 시작 도시로 보냄

    # DP 적용 -> DP캐시 값이 존재한다면 last, visited에 대한 연산이 이미 계산된 적 있다는 뜻
    # 따라서 중복 계산하지 않고 그 값을 그대로 사용
    if (dp[last][visited]):
        return dp[last][visited]

    tmp = sys.maxsize
    for city in range(N):
        if ((visited & (1 << city) == 0) and (cities[last][city] != 0)):
            if ((new := TSP(city, visited | (1 << city)) + cities[last][city]) < tmp):  # 최솟값 업데이트
                tmp = new
    
    dp[last][visited] = tmp
    return tmp


print(TSP(0, 1 << 0))
