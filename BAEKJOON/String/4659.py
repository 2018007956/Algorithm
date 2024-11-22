# Solved (20m)
def check1(password):
    if 'a' in password or 'e' in password or 'i' in password or 'o' in password or 'u' in password:
        return True
    return False

def check2(password):
    # 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다
    consonant_cnt = 0 # 자음
    vowel_cnt = 0 # 모음
    for char in password:
        if char in ['a','e','i','o','u']:
            vowel_cnt += 1
            consonant_cnt = 0
        else:
            consonant_cnt += 1
            vowel_cnt = 0


        if consonant_cnt >= 3 or vowel_cnt >= 3:
            return False
    return True
    
def check3(password):
    # 같은 글자가 연속적으로 두번 오면 안되나, ee와 oo는 허용한다.
    for i in range(1, len(password)):
        if (password[i] != 'e' and password[i] != 'o') and password[i] == password[i-1]:
            return False
    return True


while True:
    password = input()
    if password == 'end':
        break

    if check1(password) and check2(password) and check3(password):
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')