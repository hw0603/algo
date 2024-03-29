## Info
<a href="https://www.acmicpc.net/problem/9466" rel="nofollow">9466 텀 프로젝트</a>

## ❗ 풀이
기본적인 아이디어는 학생들의 선택을 방향 그래프로 보고 DFS로 그래프를 탐색한다고 생각하는 것이다.  
반복문 안엣허 1번 학생부터 마지막 학생까지를 각각 그래프의 시작 노드로 보고 깊이 우선 탐색을 진행하는데, 사이클이 만들어지는 경우에 사이클의 멤버 끼리는 같은 팀이 될 수 있으므로 해당 학생들을 모두 팀이 있는 것으로 마킹한다.  
  
이전에 방문했던 지점에 다시 도착했다면, 그 이후에는 예전에 방문했던 경로와 동일한 순서로 방문하게 될 것이다.  
이러한 중복 계산을 피하기 위하여 `checkResult` 딕셔너리를 전역으로 두고, 방문했을 때 팀을 형성할 수 있는 학생들은 `True`로, 팀을 형성할 수 없는 학생들은 `False`로 표기하고, 노드 방문 시 `checkResult` 딕셔너리에 마킹된 값(`True`/`False`에 관계없이)이 존재한다면 그 지점은 이미 방문한 지점이므로 더 이상 탐색하지 않는다.  
  
사이클 형성을 판단하기 위하여 노드 방문 시 이전에 방문했던 경로들의 기록을 순서대로 유지하고 있어야 하며, 이 기록에 이미 존재하는 노드를 다시 방문했을 때가 바로 사이클이 형성되는 시점이라고 할 수 있다.  
```
1 -> 2 -> 3 ->    4 -> 5 -> 6 ->    4 (-> 5 -> 6 ->) ...
```
과 같은 방문 기록이 있다고 할 때, 현재 노드는 `4` 이고, `history` 배열에 이미 `4`가 존재하므로, 사이클(4-5-6)이 형성됨을 알 수 있다.  
현재 노드(`4`)보다 이전에 들어온 노드 1, 2, 3에 대해서는 절대 팀을 이룰 수 없으므로 각 노드에 `False`를, 4, 5, 6에 대해서는 팀을 형성할 수 있으므로 `True`를 마킹하면 된다.  
  
이때, `history` 배열에 원소가 존재하는지 여부를 단순히 `in`연산자를 활용하여 판별하면 `in`연산의 시간복잡도는 `O(N)` 이므로, 시간초과가 나게 된다.  
이를 해결하기 위해 `history`배열 이외에 `hisdict`를 별도로 두어, `history` 배열에 `append()`할 때 마다 `hisdict`에도 키를 추가해 주면, 딕셔너리 인덱싱(`O(1)`)을 통해 존재 여부를 빠르게 판단할 수 있다.

## ❗ 추가 지식
None

## 🙂 마무리
로직 자체는 꽤 빨리 생각해 냈는데 시간과 메모리 사용량을 줄이는데 꽤 오래 걸린 문제.  
78%에서 시간초과 컷 나서 딕셔너리 추가해서 이전 히스토리들을 다 저장하는 방식으로 풀이했더니 이번엔 메모리 초과가 떴다.  
딕셔너리를 추가해서 `in`연산을 하지 않는 방식으로 개선하니 어찌어찌 통과하긴 했는데.. 더 나은 방법이 있는 걸까?