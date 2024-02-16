N = input()
score_lst = list(map(int, input().split()))

M = max(score_lst)
New_score = list(map(lambda x:x/M*100, score_lst))
print(sum(New_score)/len(New_score))