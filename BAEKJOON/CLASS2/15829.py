def Hash(s):
    M = 1234567891
    # 문자열 -> 숫자 치환: 아스키 변환 (a~z = 97~122)
    sum = 0
    for i in range(len(s)):
        a = ord(s[i])-96
        r = 31 ** i
        sum += a*r
    return sum % M

L = int(input())
print(Hash(input()))