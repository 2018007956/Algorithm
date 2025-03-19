# Solved (20m)
# 틀린 코드 - 가장 작은 길이로 자르기
def solution(phone_book):
    shortest_len = len(sorted(phone_book, key=len)[0])

    new_phone_book = []
    for x in phone_book:
        new_phone_book.append(x[:shortest_len])
    
    if len(set(new_phone_book))==len(phone_book):
        return True
    else:
        return False
'''
처음에는 위와 같이 가장 짧은 길이로 잘라서 비교했는데, 
TC에서 2개 틀림
가장 짧은 길이가 아닌 경우에서도 다른 번호에 소속되는 경우 있고, 고려해줘야 함
'''

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True
'''
접두사 확인 전략
  정렬된 상태에서는, 바로 다음 번호와만 비교하면 접두사인지 확인할 수 있다.
  예: ["12", "123", "567", "88"]에서 "12"와 "123"만 비교하면 됨.
효율성 고려
  최대 1,000,000개의 전화번호가 있으므로, 정렬이 O(n log n).
  정렬 후 접두사 검사는 한 번만 반복문을 돌리므로 O(n).
'''

# 다른 사람 풀이) Hash 사용
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer


# 다른 사람 풀이) 정규표현식 regex 사용
import re
def solution(phoneBook):
    for b in phoneBook:
        p = re.compile("^"+b) # b로 시작하는 패턴
        for b2 in phoneBook:
            if b != b2 and p.match(b2):
                return False
    return True