N = int(input())
W = list(map(int, input().split()))

def Energy(W):
    if len(W)==1:
        return
    else:
        x = len(W)//2
        if x!=0 and x!=-1:
            W.pop(x)
        return Energy(x-1) * Energy(x+1)

print()