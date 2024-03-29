## Info

<a href="https://www.acmicpc.net/problem/14002" rel="nofollow">14002 가장 긴 증가하는 부분 수열 4</a>

## ❗ 풀이
`dp[0][i]`를 `arr[i]`로 끝나는 가장 긴 증가하는 부분수열의 길이, `dp[1][i]`는 그 부분수열에서 `arr[i]` 바로 앞에 오는 수의 인덱스라고 정의하자.  
그렇다면 `dp[0]`의 원소 중 최댓값이 부분수열의 길이가 될 것이고, 그 최댓값이 존재하는 dp배열의 인덱스로부터, `dp[i][index]`를 계속 참조하여 실제 부분수열을 반대 방향으로(오른쪽에서 왼쪽으로) 구할 수 있다.  
  
문제에서 "증가하는" 부분수열에 대해 구하고 있으므로 `dp[0][idx]`의 값은 `arr[idx]`보다 작은 `arr[i]`들에 대하여, 모든 가능한 `dp[0][i]`의 경우 중 최댓값에 1을 더한 값이 된다.  
이 때, 나중에 수열을 참조하기 위해 매 경우마다 최댓값이 저장되어 있는 dp배열의 인덱스를 `dp[1]`에 저장해 준다.  
  
`dp[N-1]`이 구해질 때 까지 메인 반복문을 순회한 후 도출된 `dp[0]` 중 최댓값이 부분수열의 길이가 되며, LIS의 마지막 원소가 존재하는 인덱스 i에 대하여 `arr[dp[1][i]]`를 리스트에 저장하면서 `i = dp[1][i]`로 계속 업데이트 해 주고, 마지막에 리스트를 거꾸로 출력하면 LIS 수열이 된다.  


## ❗ 추가 지식



## 🙂 마무리
원본 수열을 어떻게 계속 유지하고 있을 지 생각하다가 처음에는 `dp[1]`에 매 시행마다 당시의 부분수열을 만들 수 있는 인덱스들을 모두 저장해 두었고, 실제로 그 방식으로 제출해서 풀이에 성공했다.  
부분적으로라도 3차원 배열을 쓰기 싫어서 다른 방법이 있을까 찾아보다가 현재 풀이와 같이 현재 시행 바로 직전의 수에 대한 인덱스만 저장해 두면 마지막에 거꾸로 타고 올라가면서 수열을 구할 수 있다는 아이디어를 얻었다.