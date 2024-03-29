## Info
<a href="https://www.acmicpc.net/problem/1915" rel="nofollow">1915 가장 큰 정사각형</a>

## ❗ 풀이
임의의 정사각형은 작은 정사각형들이 모인 집합으로 생각할 수 있다.  
`dp[i][j] = (i, j)를 오른쪽 끝으로 하는 정사각형의 최대 길이` 로 정의한다.  
현재 보고 있는 좌표의 값이 0인 경우에는 당연히 정사각형을 이어 나갈 수 없으므로 DP값 역시 0으로 설정한다.  
그 외의 경우에는 정사각형을 이어 나갈 수 있는 가능성이 있다고 보고, 나와 인접한 3개의 칸을 참조하여 현재 칸의 DP값을 구해 준다.  
  
`dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1`  

n, m에 해당하는 이중루프를 돌면서 dp값을 업데이트할 때 최댓값을 항상 비교하여 업데이트 해 주고, 루프 종료 후에 최댓값의 제곱을 출력하면 정답.

## ❗ 추가 지식
None

## 🙂 마무리
DP 점화식을 세울 때 접근은 어느 정도 맞게 했지만 처음에는 `(i, j)`가 추가될 때 `matrix`에서 `i행`과 `j열`의 값이 모두 1인지 검사를 하고 난 뒤에 DP 값을 업데이트하도록 작성했었는데, 그렇게 하니 루프가 3중으로 생겨 너무 느렸다.  
다시 생각해 보니 이미 이전의 DP 값을 구해 두었으므로, `(i, j)`가 추가될 때는 나의 왼쪽, 위쪽, 대각선 왼쪽 위. 이렇게 3칸의 DP값만을 참조하여 구해 주면 된다는 것을 발견했다.
