# Solved
def solution(numbers):
    lst = list(map(str, numbers))
    result = ''.join(sorted(lst, key=lambda x:x*3, reverse=True))
    return '0' if result[0]=='0' else result
'''
'0' if result[0] == '0' 같은 예외 처리를 떠올리기 위해선 Edge Case를 신경써야함
Edge case를 생각해내려면,
1. 문제의 제약 조건을 곱씹기
    numbers의 원소는 0 이상 1,000 이하의 정수
    => "전부 0으로만 된 입력이 가능하겠네?" 떠올릴 수 있음
2. 출력 형식을 다시 생각해보기
    문제에서는 가장 큰 숫자를 만들어야 하니까 결과는 정수처럼 보여야 함
    => 결과값이 '000'일 경우에만 특별 처리 필요하다는 걸 캐치할 수 있음
3. 테스트 케이스 최소화
    모든 원소가 0인 경우"처럼 극단적인 케이스를 만들고 결과가 이상한지 확인
'''

# 시간 초과 -> 최대 길이가 10만이다. 규칙 찾아서 정렬해야함
from itertools import permutations
def solution(numbers):
    tmp = list(permutations(map(str,numbers), len(numbers)))
    return sorted(list(map(lambda x: ''.join(x), tmp)))[-1]