import sys
input = sys.stdin.readline

def round2(num): # 파이썬 round는 오사오입이므로 틀렸습니다 뜸
    return int(num) +1 if num - int(num) >=0.5 else int(num)

n = int(input())
if n==0:
    print(0) # no op
else: # 위에 n=0인 경우 잘 빼놓고 else 안하면 런타임에러
    opinion = [int(input()) for _ in range(n)]    
    opinion.sort()
    rm = round2(n*0.15)
    if rm!=0: # rm=0인경우 고려안해줘서 런타임에러 발생
        opinion = opinion[rm:-rm]
    print(round2(sum(opinion)/len(opinion)))