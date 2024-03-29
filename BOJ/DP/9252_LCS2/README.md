## Info

<a href="https://www.acmicpc.net/problem/9252" rel="nofollow">9252 LCS 2</a>

## ❗ 풀이
<a href="https://www.acmicpc.net/problem/9252" rel="nofollow">9251 LCS</a>에서 LCS의 길이 이외에도 최종 LCS 수열 자체를 출력하는 조건이 추가된 문제이다.  
  
`dp[len(str1)][len(str2)]` 크기의 2차원 리스트를 만들고, 0행과 0열은 모두 0으로 비워 둔다.  
이 때 `dp[i][j]` 는 `str[:i+1]` 과 `str[:j+1]`로 만들 수 있는 LCS의 길이. 즉, 첫 번째 문자열의 i번째 문자 까지와, 두 번째 문자열의 j번째 문자 까지로 만들 수 있는 LCS의 길이를 의미한다.  
<br>
그렇다면 다음과 같은 점화식이 성립한다.
```
현재 시행에서 추가된 문자가 같은 경우, 
dp[i][j] = dp[i][j] = dp[i-1][j-1] + 1 # 이번 시행에서 추가된 문자를 제외한 문자열들의 LCS + 1

현재 시행에서 추가된 문자가 서로 다른 경우,
dp[i][j] = max(dp[i-1][j], dp[i][j-1]) # 각 문자들을 하나씩 제외한 문자열들의 LCS 길이 중 최댓값
```
루프 종료 이후 `dp[-1][-1]`을 구하면 LCS의 길이가 된다.
  
LCS 원본 수열을 복원하기 위하여 `dp[-1][-1]`에서부터 시작하여 거꾸로 타고 올라가며 dp 배열을 조사한다.  
이때, dp 배열을 생성하는 규칙을 거꾸로 적용하여 `str1[i]`와 `str2[j]`가 같을 경우에는 `dp[i-1][j-1]`로 이동하고, 두 문자가 다를 경우에는 `dp[i-1][j]` 와 `dp[i][j-1]` 중 큰 곳으로 이동한다.  
이동은 i 혹은 j가 0이 될 때 까지 계속 반복하며, 1회 시행 이후 변화한 `i`, `j`에 대하여 `dp[i][j]`의 값이 1 감소했다면 해당 인덱스 정보를 리스트에 저장해 둔다.  
루프 종료 이후 저장된 리스트를 거꾸로 참조하여 출력하면 원본 수열을 구할 수 있다.

## ❗ 추가 지식


## 🙂 마무리
처음에는 <a href="https://www.acmicpc.net/problem/14002" rel="nofollow">14002 가장 긴 증가하는 부분 수열 4</a>를 풀었을 때 처럼 매 시행마다 이전 시행의 인덱스 정보를 남겨 두고, 마지막에 그 인덱스를 따라 거슬러 올라가는 방법으로 풀이하려고 했다. 물론 그렇게 풀어도 되지만 14002번과 달리 이번에는 dp배열로 2차원 배열을 사용하므로 행과 열 정보 모두를 저장해야 하고, 코드가 깔끔해지지 않았다. 표를 그려서 잘 살펴 보니 인덱스 저장 없이도 거슬러 올라갈 수 있는 규칙을 찾을 수 있었고, 그 규칙을 적용하여 원본 수열을 성공적으로 복원할 수 있었다. 2차원 배열을 사용하는 DP 문제는 표 그리는게 조금 귀찮을 수 있지만 테스트케이스 하나 정도는 꼭 그려서 생각을 해 보자!
