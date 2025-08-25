def solution(user_id, banned_id):
    def isSame(user, ban):
        if len(user)!=len(ban):
            return False
        
        for i in range(len(user)):
            if ban[i]=='*':
                continue
            else:
                if user[i]!=ban[i]:
                    return False
        return True
        
    able = {i: [] for i in range(len(banned_id))}

    for i, ban in enumerate(banned_id):
        for user in user_id:
            if isSame(user, ban):
                able[i].append(user)
                
    AllList = []
    def dfs(a, i): # a : 현재까지 선택된 사용자 리스트
        if i == len(banned_id):
            AllList.append(a)
            return

        # able[i] : i번째 banned_id에 매칭될 수 있는 user_id 리스트
        for user in able[i]:
            if user not in a:
                dfs(a+[user], i+1)

    dfs([], 0)

    return len(set(map(tuple, map(sorted, map(list, AllList)))))
