## Info

<a href="https://www.acmicpc.net/problem/1520" rel="nofollow">1520 내리막 길</a>

## ❗ 풀이
기본적으로 DFS를 사용하여 탐색을 하고, 재귀스택 낭비를 막기 위해 한 번 방문했던 곳은 DP를 활용하여 미리 저장된 값을 불러오는 방식으로 풀이한다.  
크기가 동일한 matrix 배열(지도)과 dp 배열(방문 확인용)을 선언해 두고, dp배열의 초기값은 -1(미방문)으로 설정한다.  
  
(0, 0) 좌표에서부터 dfs 탐색을 시작하는데, 이때 현재의 좌표가 이미 방문했던 곳이라면 dp 배열에 저장된 값을 불러와 반환하고,  
처음 방문하는 곳이라면 dp 배열의 값을 0으로 설정한 다음 현재 좌표 기준 상하좌우 4방향에 대하여 조건에 맞는 좌표들에서부터 다시 dfs 탐색(재귀호출)하여 각 좌표의 경우의 수를 현재 좌표에 더해 준다.  
  
어떤 한 좌표에서의 목적지로 가는 경우의 수가 한 번 정해지면, 그 이후로는 해당 좌표에 대한 경우의 수는 변하지 않는다는 것이 포인트. 이 점을 활용하여 DP로 중복 계산을 피할 수 있다.

## ❗ 추가 지식
백준에서 `RecursionError` 가 발생하는 경우 `sys.setrecursionlimit()` 을 호출하여 최대 재귀스택 깊이를 임의로 설정해 줄 수 있다.

## 🙂 마무리
처음에는 단순 DFS로 풀었다가 (당연히) 메모리 초과가 떠서 DP를 어떻게 적용해야 하나 고민해 보았고, 중복 계산되는 지점을 파악하긴 했지만 구현을 어떤 식으로 해야 할지 몰라서 풀이를 찾아 보고 힌트를 얻어서 풀었다. DP에서 그래프 문제로 넘어가는 첫 문제인데 많은 연습이 필요할 듯..
