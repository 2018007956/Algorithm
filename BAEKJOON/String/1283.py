# Solved (1h 10m) w/ Search
N = int(input())
dic = {}
for _ in range(N):
    option = input()
    words = option.split()
    result = option
    # 1. 단어의 첫 글자
    for idx, word in enumerate(words):
        if word[0].upper() not in dic:
            dic[word[0].upper()] = 1
            words[idx] = '[' + word[0] + ']' + word[1:]
            result = ' '.join(words)
            break
    # 2. 왼쪽부터 알파벳 탐색
    else:
        for idx, alphabet in enumerate(option):
            if alphabet!=' ' and alphabet.upper() not in dic:
                dic[alphabet.upper()] = 1
                result = option[:idx] + '[' + alphabet + ']' + option[idx+1:]
                break
    
    print(result)
'''
4:22~46 (24m) 런타임 에러 TypeError
    str(*words[idx+1:]) 부분에서 발생 
    *는 함수에 인자로 리스트의 요소를 풀어주는 역할을 하지만, str() 함수는 여러 인자를 받지 않기 때문에 에러가 발생
    따라서 리스트 요소를 문자열로 적절히 결합해야 함

~32 (46m) 틀렸습니다
    반례 : https://www.acmicpc.net/board/view/127533
    빈칸 처리
'''