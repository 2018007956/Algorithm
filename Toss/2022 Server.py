# https://toss.im/career/article/next-developer-2023-sample-questions
# Solved (18m)
s = input()
d = []
cnt = 1
for i in range(1, len(s)):
    if s[i-1]==s[i]:
        cnt += 1
    else:
        cnt = 1

    if cnt==3:
        d.append(int(s[i-1]*3))

if d:
    print(max(d))
else:
    print(-1)


# 모범 답안
max_val = -1
for i in range(len(s)-2):
    if s[i]==s[i+1] and s[i+1]==s[i+1]:
        max_val = max(max_val, int(s[i]*3))
print(max_val)