# 풀이 공부
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

preorder = []
while True:
    try:
        x = int(input())
        preorder.append(x)
    except:
        break

def build_postorder(preorder):
    if not preorder:
        return []
    
    root = preorder[0]
    idx = len(preorder) # root보다 큰 값이 없는 경우 처리

    for i in range(1, len(preorder)):
        if preorder[i] > root:
            idx = i
            break
    
    left = build_postorder(preorder[1:idx])
    right = build_postorder(preorder[idx:])
    
    return left + right + [root]


postorder = build_postorder(preorder)
print('\n'.join(map(str, postorder)))

'''
또는 26~33줄 코드를 아래와 같이 구현해도 됨

    build_postorder(preorder[1:idx])
    build_postorder(preorder[idx:])
    print(root)

build_postorder(preorder)
'''