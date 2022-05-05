from bisect import bisect_left
from math import ceil, sqrt
import sys


N = int(sys.stdin.readline())
coords = list({tuple(map(int, sys.stdin.readline().split())) for _ in range(N)})  # set iteration

# 두 점의 좌표를 전달받고 거리의 제곱 반환
def getdist(p1: tuple, p2: tuple) -> int:
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2


def solve(l: int, r: int, arr: list, return_to_main=False) -> list:
    diff = r - l
    # 점이 두 개일때는 그 두 점 사이의 거리가 최솟값
    # 이때, 두 점의 y좌표를 비교하여 정렬하고 반환해 준다
    if (diff == 2):
        if (arr[0][1] > arr[1][1]):
            arr[0], arr[1] = arr[1], arr[0]  # 대소비교 후 swap 하여 정렬. O(1)
        return [getdist(coords[l], coords[r-1]), arr]
    # 점이 세 개일때는 3C2 경우 중 거리의 최솟값이 정답
    elif (diff == 3):
        return [min(
            getdist(coords[l], coords[l+1]),
            getdist(coords[l+1], coords[l+2]),
            getdist(coords[l+2], coords[l])
        ), sorted(arr, key=lambda x: x[1])]

    mididx = (l + r) // 2
    mid_x = coords[mididx][0]  # 점들의 개수를 반으로 분할하는 세로선 구함

    # 재귀함수 호출하여 분할된 평면의 좌우에서 최솟값과 그때 정렬된 리스트 구함
    l_min, l_arr = solve(l, mididx, arr[:len(arr)//2])
    r_min, r_arr = solve(mididx, r, arr[len(arr)//2:])

    # 분할된 2개의 평면에서 각각 최근접점 쌍의 거리의 최솟값을 d로 저장
    d = min(l_min, r_min)

    # y좌표 기준으로 정렬된 l_arr과 r_arr을 병합
    # 단순 병합이므로 시간복잡도는 O(N)
    i, j = 0, 0
    len_l = len(l_arr)
    len_r = len(r_arr)
    sorted_arr = []
    if not (return_to_main): # 현재 재귀에서 메인함수로 리턴하는 경우 병합된 리스트를 사용할 일이 없으므로 병합하지 않음
        while (i < len_l and j < len_r):
            if l_arr[i][1] <= r_arr[j][1]:
                sorted_arr.append(l_arr[i])
                i += 1
            else:
                sorted_arr.append(r_arr[j])
                j += 1

        while (i < len_l):
            sorted_arr.append(l_arr[i])
            i += 1
        while (j < len_r):
            sorted_arr.append(r_arr[j])
            j += 1

    # x 좌표 기준으로만 비교해도 분할선과의 거리가 d보다 먼 경우는 제외하고 후보군 선정
    # l_arr과 r_arr이 이미 정렬된 상태이므로 별도의 정렬 불필요
    # 좌우에 맞게 후보군으로 좌표를 삽입 -> bisect 사용할 것이므로 y좌표를 첫 인덱스로 넣음
    # -------------------------------------------------------------------------------------
    # 재귀에서 mididx를 기준으로 좌우를 분할해 주었으므로, 지금처럼 병합정렬 사용하지 않고 단순히 원본 좌표에서 좌우를 분할할 경우,
    # mididx 기준으로 분할해 주어야 재귀에서 놓친 쌍(ex. 최소인 두 점이 모두 분할선 위에 존재하는 경우 등)들을 확인하고 넘어갈 수 있음.
    # 단순히 x좌표와 mid_x를 대소비교하여 좌우 후보군을 나눈다면 위와 같은 케이스의 경우 같은 평면상에 존재하는 것으로 인식하여 확인하지 않고 넘어가게 됨
    l_candidate = [(p[1], p[0]) for p in l_arr if ((mid_x - p[0])**2 < d)]  # idx가 mididx보다 작은 점들
    r_candidate = [(p[1], p[0]) for p in r_arr if ((mid_x - p[0])**2 < d)]  # idx가 mididx보다 크거나 같은 점들

    min_dist = d # 현재까지 구해진 거리의 최솟값
    
    for y1, x1 in l_candidate: # 좌측 후보군에서 점 하나씩 가져와서
        rt = ceil(sqrt(min_dist))  # min_dist는 거리의 제곱 값이므로 연산을 위해 제곱근을 취하고, 오차 발생의 여지가 있으므로 올림하여 조사범위를 살짝 넓혀 줌
        bottom_left = bisect_left(r_candidate, (y1-rt, -sys.maxsize))  # 좌측 하단 lower_bound
        top_right = bisect_left(r_candidate, (y1+rt, sys.maxsize))  # 우측 상단 upper_bound
        for y2, x2 in r_candidate[bottom_left:top_right]: # 우측 후보군이랑 비교를 하는데, 조건을 만족하는 범위에 대해서만 비교함
            min_dist = min(min_dist, getdist((x1, y1), (x2, y2)))

    return [min_dist, sorted_arr]


if (len(coords) != N):  # N과 개수가 같지 않으면 중복점이 있다는 뜻이므로 최소 거리는 0
    print(0)
else:  # 중복점이 없는 경우 계산 수행
    coords.sort()  # x좌표 기준 정렬. O(NlogN)
    print(solve(0, N, coords, return_to_main=True)[0])
