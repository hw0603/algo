## Info
<a href="https://www.acmicpc.net/problem/9251" rel="nofollow">9251 LCS</a>

## ❗ 풀이
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
루프 종료 이후 `dp[-1][-1]`을 구하면 답이 된다.


## ❗ 추가 지식
파이썬의 `str.split()` 은 empty separator를 지원하지 않는다. 공백 없는 문자열에서 문자 단위로 분리하고 싶을 때는 `list(str)`를 사용하자.  
문자열 비교 보다 정수형 비교가 더 빠를 것 같아서 처음에 문자열 데이터를 받을 때 `ord()`를 통해 아스키 코드 리스트 형태로 변환하여 보았는데, 실행시간 차이가 그리 크지 않았다.(672ms vs 676ms) 문자열 비교는 당연히 정수형 비교보다 느리지만, 이 문제의 경우 문자열 자체를 비교하는 것이 아니라 루프 안에서 문자 하나를 비교하므로 성능 개선이 크지 않은 것으로 판단했다.



## 🙂 마무리
며칠동안 고민하다가 정답이 안 보여서 풀이를 찾아 봤다. 2차원 dp배열을 생성하는 접근 자체는 비슷하게 했지만, 배열을 채울 때 두 가지 조건으로 나누어 생각하는 것을 놓치고 있었다.  
dp문제인 이상 이전 시행을 어떻게 활용해야 할지를 고민해야 하는데, 여러 조건을 두고 잘 생각해 봐야 할 것 같다.  