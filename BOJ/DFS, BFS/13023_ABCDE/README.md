## Info
<a href="https://www.acmicpc.net/problem/13023" rel="nofollow">13023 ABCDE</a>

## ❗ 풀이
<a href="https://www.acmicpc.net/problem/2668" rel="nofollow">2668 숫자고르기</a>와 유사한 문제.  
사람 수 크기의 리스트를 만들어 두고, 친구 리스트를 입력받으면서 각자의 원소로 그들의 친구 정보를 저장해 둔다.  
저장이 끝나면 첫 번째 사람부터 dfs 탐색을 시작하고, dfs 안에서는 5명이 연결되어야 하므로 현재 상태에서 연결된 친구들의 정보를 저장하기 위한 `friendlink`를 사용한다. 연결된 친구들의 정보는 각 재귀 깊이마다 고유한 값이므로, `friendlink`를 자식 dfs로 전달할 때는 `[:]`등을 이용하여 복사본을 넘겨주어야 한다.

## ❗ 추가 지식


## 🙂 마무리
모든 사람들에 대하여 dfs탐색을 해 줘야 하는데 처음에 그냥 dfs(0)만 하고 제출해서 틀렸다. 이런거 제출 전에 좀 더 생각하고 풀자.  
다른 사람들에 비해 실행속도가 좀 느리다. 그리고 `sys.exti()` 시킨 거 뭔가 맘에 들지 않는다. 개선할 수 있는 방법이 있지 않을까?