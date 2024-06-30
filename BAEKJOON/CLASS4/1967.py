# 4h 25m 풀었지만 시간 초과 / 풀이 공부
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    s, e, w = map(int, input().split())
    tree[s].append((e, w))
    tree[e].append((s, w))
# weight를 따로 담을 필요 없이 tree에 tuple로 함께 넣음

# 연결된 노드 중 방문하지 않은 노드 방문
def dfs(start, distance):
    for next, next_d in tree[start]:
        if visited[next] == -1:
            visited[next] = distance + next_d
            dfs(next, visited[next])

# 시작 정점에서 임의의 정점까지의 거리를 구하고 그 중 가장 먼 거리를 구한다
visited = [-1] * (n+1)
visited[1] = 0
dfs(1, 0)

# 위에서 찾은 노드에 대해 가장 먼 노드를 찾는다
# 가장 먼 노드를 시작지점으로 하여 다시 한번 가장 긴 거리를 찾는다
last_node = visited.index(max(visited))
visited = [-1] * (n+1)
visited[last_node] = 0
dfs(last_node, 0)

print(max(visited))

'''
leaf node부터 출발해서 모든 경우의 수 고려하며 max_value 갱신?
leaf node 찾는 법 : 자식이 없기 때문에 연결된 노드가 부모 하나 밖에 없음

10:57~06, 15~35, 41~25, 30~38 (1h 21m) 2% 시간 초과
    모든 리프 노드에서 전부 시작하면 시간초과고, 답이 될 수 있는 특정 노드에서 시작할 수 있도록 알고리즘을 구성해야 한다.
    모든 경우를 탐색 안하고 미리 특정 길이 max일 것이라고 알 수 있는 방법이 있나?
    -> 부모가 같은 리프노드는 탐색 경로가 같다!!
    -> 리프노드의 부모 노드부터 탐색하여 얻은 max 값과 두 리프 노드의 값 중 더 큰 값을 더함

~31 (53m) 2% 시간 초과
    9->5->3->6->12 계산했으면, 거꾸로 12->6->3->5->9는 계산되지 않게
    -> leaf node 부터 탐색이 아니라 leaf node가 아닌 노드들을 탐색하면서 leaf node까지의 거리를 측정해야할까?
    루트 부터 시작해서 left tree, right tree 중 max 값을 각각 구해서 더하는 방식으로 구현 // left right 어떻게 알지? -> dfs 각각 탐색
    -> 왜 틀렸을까? 알고리즘 어디가 잘못됐지..?
    -> root, left tree, right tree max 값을 각각 출력해보니 root 1은 괜찮은데 2부터 이상한 값 출력됨

5:04~30, 33~6:01 (54m) 8% 틀렸습니다.
    child 노드만 고려되어야 하는데, 부모 노드까지 고려되는게 문제였음,
    부모 노드 제외하는 코드 작성 (child list 생성)

~13, 8:48~59 (23m) 2% 틀렸습니다.
    반례 보기 전에 알고리즘 적으로 이상한 부분이 있는지 생각해보기.
    이 알고리즘으로 짰을 때 고려 안되는 경우의 수가 있나?
    알고리즘 적 오류를 도저히 모르겠어서 질문게시판을 확인해봤더니,
    <부모노드보다 자식노드의 번호가 작을 수도 있다>는 것을 알았다
    반례) 3 / 1 3 2 / 3 2 1
    -> node 3의 child list에 들어오는게 없어서 IndexError 발생
    
    그러면 부모인지 자식인지는 어떻게 알 수 있을까? "visted"

9:06~25 (19m) 2% 틀렸습니다.
    질문게시판을 보고 또 하나 놓친 점 발견 : 이진 트리가 아니다
    반례) 4
    1 2 3
    1 3 1
    1 4 2
    정담) 5
    출력) 3
    주어진 예시만 보며 풀다가, 예시의 구조밖에 고려하지 못하게 됨. 

~45 (20m) 32% 시간 초과
    from_leaf_weight를 리스트에서 max값 가지는 변수로 변환 // 똑같이 32% 시간 초과
~55 (10m) PyPy3로 돌려봄 => 2% 메모리 초과......
    PyPy3의 경우 sys.setrecursionlimit은 "주어진 깊이만큼의 재귀를 충분히 수행할 수 있는" 크기의 메모리를 미리 할당받는 역할을 합니다. 
    여유 있게 잡기 때문에 100만 번의 재귀를 허용하기 위해서 받는 메모리의 양은 어마어마하고, 그 즉시 문제에 주어진 메모리 제한을 초과하게 됩니다.
    이 문제에서는 n이 1만 이하라 100만까지 필요하지 않습니다. 그냥 10**4만큼만 잡아주면 됩니다.

~10:00 (5m) PyPy3로 해도 똑같이 32% 시간 초과
    leaf node 제외 모든 노드를 돌면서 leaf 까지의 weight를 재귀함수 호출로 계산한다 -> 각 노드에서 자식 노드 수만큼 dfs 호출하므로, 최악의 경우 O(N^2)

(시간 초과 코드)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

n = int(input())
tree = [[] for _ in range(n+1)]
weight = {}
for _ in range(n-1):
    s, e, w = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)
    weight[(s,e)] = w
    weight[(e,s)] = w

def dfs(cur: int, child: list, cur_weight: int):
    global from_leaf_weight
    if len(tree[cur])==1: # leaf node 도착하면 종료
        from_leaf_weight = max(from_leaf_weight, cur_weight)
        return 
    
    for n in child:
        if not visited[n]: # 온 길 제외, # 상위 노드 고려 X
            visited[n] = True
            # print('--',cur, n, cur_weight)
            dfs(n, tree[n], cur_weight + weight[(cur, n)]) # 다른 길로 확장
            visited[n] = False

# print(tree)
# visited_parent = {}
result = 0
visited = [False] * (n+1)
for idx, node in enumerate(tree):
    max_value = 0

    
    #리프 노드부터 남색하는 방법 -> 시간 초과
    # if len(node)==1:
    #     if tree[idx][0] not in visited_parent:
    #         visited[idx] = True
    #         visited[tree[idx][0]] = True
    #         dfs(tree[idx][0], tree[tree[idx][0]], 0) # 시작 리프 노드와 그 부모 노드 사이의 weight는 계산 X -> 추후 else 문에서 비교하기 위해 / 그러면 start를 안넣어도 됨
    #         visited_parent[tree[idx][0]] = max_value
    #     else:
    #         cmp_lr = max(visited_parent[tree[idx][0]]+weight[(idx-1,tree[idx][0])], visited_parent[tree[idx][0]]+weight[(idx,tree[idx][0])])
            
    #         result = max(result, cmp_lr)
    

    if idx!=0 and len(node)!=1:
        # print('root:',idx)
        visited[idx] = True
        child = [x for x in tree[idx] if not visited[x]]

        candidate_max = []
        for i in range(len(child)): # 이진 트리가 아니라 자식이 3 이상일 수 있음
            from_leaf_weight = 0
            visited[child[i]] = True
            dfs(child[i], tree[child[i]], 0)
            candidate_max.append(from_leaf_weight + weight[(idx, child[i])])
        
        candidate_max.sort(reverse=True)
        max_value = sum(candidate_max[:2])
        
        result = max(result, max_value)


print(result)

11:58~ 정답 코드 공부
    트리 내에서 가장 긴 경로인 트리의 지름은
    <한 노드에서 시작해서 가장 먼 노드를 찾고, 그 노드에서 다시 가장 먼 노드를 찾는 방법>으로 구할 수 있다.
'''