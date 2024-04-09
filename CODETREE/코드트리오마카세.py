# 	삼성 SW 역량테스트 2023 하반기 오후 2번 문제 
def check_waiting_customers(belt, stand_by, time_clock): 
    for sit, val in stand_by.copy().items(): 
        try:
            cus = list(val.keys())[0] # 이 구조 하나하나 출력해보면서 이렇게 짜는게 맞나. 시험장에선 못할듯. 어떻게 해야하지.
            num = int(list(val.values())[0])

            # rotate_belt = [(k+time_clock)%L for k in list(belt.keys())]
            # belt_idx = rotate_belt.index(sit)
            # rotate = list(belt.values())[belt_idx]
            key_idx = (sit-time_clock+L)%L # stand_by 의 위치번호를 고정된 belt 위치로 맞춰줘야됨
            print('--',sit, key_idx)
            if cus in list(belt[key_idx].keys()): 
                if belt[key_idx][cus] >= num:
                    belt[key_idx][cus]-=num
                    del stand_by[sit]
                else:
                    stand_by[sit][cus]-=belt[key_idx][cus]
                    del belt[key_idx][cus]
                
            # value 0인 리스트 정리
            if belt[key_idx][cus]==0: 
                del belt[key_idx][cus]
            # value가 빈 리스트인 key값 정리
            if not belt[key_idx]:
                del belt[key_idx]
        except:
            pass
    
    # # stand_by = {k:v for k, v in stand_by.items() if v.values()!=0}  -> 안됨. 아래와 같이 구현 필요. 
    # # del stand_by[sit] 하게 되면 RuntimeError: dictionary changed size during iteration 발생해서 for sit,val in stand_by.items().copy() 해줘야 됨 (이게 조금 더 시간 단축되서 이 방법 사용)
    # stand_by = {k: {name: count for name, count in v.items() if count != 0} for k, v in stand_by.items()}
    # stand_by = {k: v for k, v in stand_by.items() if v} # value가 빈 리스트인 key값 정리
    return belt, stand_by

L, Q = map(int, input().split()) # L: 초밥 벨트 길이, Q: 명령 수
belt = {}
stand_by = {}
time_cnt = 1
clock = 0
for i in range(Q):
    val = input().split()

    if val[0] == '100': # 초밥 만들기
        t, x, name = val[1:]
        x = int(x)
        try:
            if name in list(belt[(x-clock+L)%L].keys()): # name 열 추출
                belt[(x-clock+L)%L][name]+=1
            else:
                belt[(x-clock+L)%L][name]=1
        except:
            belt[(x-clock+L)%L]={name:1}
    elif val[0] == '200': # 손님 입장
        t, x, name, n = val[1:]
        t, x, n = int(t), int(x), int(n)
        stand_by[x]= {name: n}


    
    clock += 1
    for i in range((int(val[1])-time_cnt)%L):
        # belt = dict(((key+1)%L, value) for (key, value) in belt.items()) # dict을 직접 회전하지 않고 index를 조정하는 방향으로 구현
        belt, stand_by = check_waiting_customers(belt, stand_by, clock+i) # 매 초마다 waiting 고객이랑 belt 매칭 확인
    time_cnt = int(val[1])

    print('>> belt: ',belt, 'stand_by: ',stand_by)
    
    if val[0] == '300': # 사진 촬영
        print(len(stand_by.keys()), sum([k for nested in belt.values() for k in nested.values()])) # 사람 수, 초밥 수

    

    
'''
[첫번째 시도] 1h 35m : 시간초과
Constraints:
    3 ≤ L ≤ 1,000,000,000
    1 ≤ Q ≤ 100,000
    1 ≤ t ≤ 1,000,000,000
    0 ≤ x ≤ L−1
    1 ≤ name 의 길이 ≤ 30
    1 ≤ 주어지는 서로 다른 name의 수 ≤ 15,000
Discussion:
    - query로 접근하는게 핵심인 것 같다
    - 이 문제는 직접 회전하지 않고, 각 스시가 언제 들어와서 언제 사라지는지를 손님이 가게에 들어오는 시간을 기준으로 수학적으로 계산하되, 
    시간순서대로 이를 처리하기 위해 우선순위큐를 이용하는 방향으로 고민해보시면 도움이 될 것 같습니다 :)
    - 코드를 작성하시기 전에 자신이 짜려는 코드의 시간복잡도, 공간복잡도를 미리 정의해보는 습관이 매우 중요합니다.
    해당문제에서는 L이 최대 10억 까지 주어지기때문에 L에 관련된 시간복잡도, 공간복잡도는 가지면 안됩니다.

아래 테스트케이스에서 시간 초과 발생
3 1
300 403168291

[두번째 시도] 30m : 런타임에러 (MemoryError)
=> time interval 만큼 테이블 회전 시켰던 것을 (int(val[1])-time_cnt)%L 만큼 회전 시키는 것으로 바꿔줌
(수정 전 코드)
while time_cnt != int(val[1]):
    belt.appendleft(belt.pop()) # 테의블 회전 
    time_cnt += 1
(수정 후 코드)
if time_cnt != int(val[1]):
        for _ in range((int(val[1])-time_cnt)%L):
            belt.appendleft(belt.pop()) # 테의블 회전 
    time_cnt = int(val[1])

아래 테스트케이스에서 메모리 에러 발생
1000000000 100000
300 8085
 ...
Hint) Map을 잘 사용하셔서 공간복잡도를 효율적으로 활용해야합니다 :)

[세번째 시도] 4h 10m 시간 초과
L에 대해서 포문을 돌며 빈 belt 리스트 생성
(수정 전 코드)
deque([[] for _ in range(L)])
(수정 후 코드)
deque(map(lambda _: [], range(L)))
=> 비슷한듯
L 크기만큼 다 만들어 놓는 것은 비효율적인 것 같음
필요한 큐에 넣을 수 있도록 구현할 수 있을까?
빈자리도 반영을 해줘야 하는데.
dictionary로 key: 자리, value: name으로 구현해보기
 * dictionary 젤 왼쪽에 값 넣는 방법 : 새 키-값 쌍을 만들고, original dict을 뒤에 추가

"belt를 dict으로 구현"
시도3.1) stand_by 쓰지 않고 belt 안에서 +,- 로 구분 
 => 초밥이 놓인 곳에 다른 사람이 앉아있으면? => 초밥이랑 손님을 분리해야됨
시도3.2) belt, stand_by 구현 / belt는 이름을 무한정 넣어주는 것이 아닌, 숫자로 cnt
 => 아래 케이스에서 시간 초과
 1000000000 100000
 300 8085
  ...

[네번째 시도] 6h 30m
for문 분리 및 개선 작업
- stand_by 비교해서 belt 뺄 때 while 문 쓰지 않아도 됨
- 시간 복잡도
명령 처리 : O(Q)
대기 사람 체크 (check_waiting_customers 함수) : O(Q)
=> O(N)
- 공간 복잡도 : O(Q)

아닌가???
3.2 solution 이랑 거의 비슷하게 시간 초과 뜸
개선1) dict.copy() 사용 안함
결과) 시간 비슷 (테스트 케이스 시간 비교)

개선2) 리스트와 튜플의 변환: list(zip(*belt[j]))[0]와 같은 구문은 belt의 각 항목을 튜플로 변환하고 다시 리스트로 변환하는 과정. 
    이는 매우 비효율적이며, 특히 큰 데이터 세트에서 시간 소모가 큼.
결과) 시간 비슷한데 12ms 감소

개선3) a = {3: [['sam', 1], ['teddy', 1]], 2: [['june', 1]]} 이 형태로 구현되어 있어서 숫자를 개산하려할 때 zip이 너무 많이 쓰이는데, 
{3: {'sam': 1, 'teddy': 1}, 2: {'june': 1}} 이렇게 중첩 딕셔너리로 구현해보기
결과) 구조가 많이 개선돼서 될줄 알았는데 시간 초과

개선4) belt = dict(((key+1)%L, value) for (key, value) in belt.items())
-> 회전하는게 아니라 dict에서 key를 전부 1씩 증가하도록 구현해서 시간 많이 소요되지 않을 거라 생각했는데,
각 회전 시마다 모든 항목을 순회하며 새 키를 계산하고 새 딕셔너리를 생성하기 때문에, 벨트의 길이(L)가 길거나 회전이 자주 발생할 경우 비효율적일 수 있다고 함
이 부분에서 for문 돌릴 필요 없음. int(val[1])-time_cnt) 차이로 계산
=> 시간 초과는 해결 => 아니다. 매 시간마다 waiting 손님을 계산해줘야됨
"dictionary를 새로 할당해주지 않고, index를 바꾸는 방식으로 접근"
사람이 착석하는 위치 x는 그대로 두고, 테이블 번호를 확인할 때, time_clock에 따라 회전 값을 계산해줘서 회전된 테이블 번호로 접근하도록!!!
=> 값이 생각과 다르게 나오는데, 무슨 문제인지 모르겠음.... => 이 코드가 젤 위에 구현된 코드.
'''





# # ################################### Solution2 #####################################
# # 메모리 에러 발생
# # 대기 손님 중 먹을 수 있는 사람 체크
# from collections import deque
# import itertools
# def check_waiting_customers(belt, stand_by): 
#     for j in stand_by.copy(): # .copy() 안하면 RuntimeError: dictionary changed size during iteration 발생
#         if stand_by[j][0] in belt[j]:
#             while belt[j]:
#                 belt[j].remove(stand_by[j][0])
#                 stand_by[j][1] -= 1 
#                 if stand_by[j][1] == 0:
#                     del stand_by[j]
#                     break
#     return belt, stand_by

# L, Q = map(int, input().split()) # L: 초밥 벨트 길이, Q: 명령 수
# belt = deque(map(lambda _: [], range(L)))
# stand_by = {}
# time_cnt = 1
# for i in range(Q):
#     val = input().split()
#     if time_cnt != int(val[1]):
#         for _ in range((int(val[1])-time_cnt)%L):
#             belt.appendleft(belt.pop()) # 테이블 회전 
#     time_cnt = int(val[1])

#     if val[0] == '100': # 초밥 만들기
#         t, x, name = val[1:]
#         x = int(x)
#         belt[int(x)].append(name)
#         if name == belt[x][0]: # 이미 하나가 놓여있는 경우
#             belt[x][1]+=1
#         else:
#             belt[x]=[name,1]
#     elif val[0] == '200': # 손님 입장
#         t, x, name, n = val[1:]
#         t, x, n = int(t), int(x), int(n)
#         for j in range(n): # check함수가 있으니 이 부분 필요없음 그냥 stand_by에 넣어주면 됨
#             try:
#                 belt[x].remove(name)
#                 n -= 1
#             except:
#                 stand_by[x]= [name, n]
#     elif val[0] == '300': # 사진 촬영
#         t = val[1:] 
#         belt, stand_by = check_waiting_customers(belt, stand_by)
#         print(len(stand_by), len(list(itertools.chain(*belt)))) 

#     belt, stand_by = check_waiting_customers(belt, stand_by)


# # ################## Solution3.1 : stand_by 쓰지 않고 belt 안에서 +,- 로 구분 #################################
# # 알고리즘 상 문제 발생 & 리스트 다루는게 넘 복잡
# from collections import deque
# import itertools
# L, Q = map(int, input().split()) # L: 초밥 벨트 길이, Q: 명령 수
# belt = {}
# time_cnt = 1
# for i in range(Q):
#     val = input().split()
#     if time_cnt != int(val[1]):
#         for _ in range((int(val[1])-time_cnt)%L):
#             belt = dict(((key+1)%L, value) for (key, value) in belt.items() if value>0)
#             # 테이블 회전 : key값 증가//근데 사람은 key값 증가하면 안됨 
#             # 문졔) 초밥이 놓인 곳에 다른 사람이 앉아있으면 그건 회전을 해야하나? => 초밥이랑 손님을 분리해야겠다
#     time_cnt = int(val[1])

#     if val[0] == '100': # 초밥 만들기
#         t, x, name = val[1:]
#         x = int(x)
#         # belt[int(x)].append(name)
#         try:
#             if name in list(zip(*belt[x]))[0]: # name 열 추출
#                 idx = list(zip(*belt[x]))[0].index(name) # list(zip(*belt[x])) : [(names), (nums)]
#                 belt[x][0][idx]+=1
#             else:
#                 belt[x].append([name,1])
#         except:
#             belt[x]=[[name,1]]
#     elif val[0] == '200': # 손님 입장
#         t, x, name, n = val[1:]
#         t, x, n = int(t), int(x), int(n)
#         for _ in range(n): 
#             try:
#                 if name in list(zip(*belt[x]))[0]: # name 열 추출
#                     idx = list(zip(*belt[x]))[0].index(name) # list(zip(*belt[x])) : [(names), (nums)]
#                     belt[x][0][1]-=1
#                 else:
#                     belt[x].append([name,-1])
#             except: # 먹을 초밥이 없는 경우
#                 belt[x]=[[name,-1]]
#                 # stand_by[x]= [name, n]
#     elif val[0] == '300': # 사진 촬영
#         t = val[1:] 
#         # a.values() -> [[['s', 1], ['t', 1]], [['j', 1]]] 
#         # ->  list(itertools.chain(*a.values())) -> [['s', 1], ['t', 1], ['j', 1]]
#         # -> list(zip(*(itertools.chain(*a.values())))) -> [('s', 't', 'j'), (1, 1, 1)]
#         res = list(zip(*(itertools.chain(*belt.values()))))[1]
        
#         pos = sum([x for x in res if x>0])
#         neg = sum([x for x in res if x<0])
#         print(neg, pos)
#         # belt, stand_by = check_waiting_customers(belt, stand_by)
#         # print(len(stand_by), len(list(itertools.chain(*belt)))) 

#     # belt에서 0인 것들 제거 ## 코드 확인 필요 (일단 없어도 돌아가기에 주석처리하고 구현중)
#     # for x, v in belt.items():
#     #     for n in list(itertools.chain(*v)):
#     #         if n[1] == 0:
#     #             idx = list(zip(*belt[x]))[1].index(0)
#     #             belt[x].remove(idx)
#     # belt, stand_by = check_waiting_customers(belt, stand_by)
#     print(belt)




# ############################################ Solution3.2 #############################################
# # 시간초과
# from collections import deque
# import itertools

# def check_waiting_customers(belt, stand_by): 
#     for j in stand_by.copy(): # .copy() 안하면 RuntimeError: dictionary changed size during iteration 발생
#         try:
#             if stand_by[j][0] in list(zip(*belt[j]))[0]:
#                 idx = list(zip(*belt[j]))[0].index(stand_by[j][0]) 
#                 while belt[j][idx][1]!=0:
#                     belt[j][idx][1]-=1
#                     stand_by[j][1] -= 1 
#                     if stand_by[j][1] == 0:
#                         del stand_by[j]
#                         break
                
#                 # value 0인 리스트 정리
#                 if belt[j][idx][1]==0: 
#                     belt[j].pop(idx)
#                 # value가 빈 리스트인 key값 정리
#                 if not belt[j]:
#                     del belt[j]
#         except:
#             pass
#     return belt, stand_by

# L, Q = map(int, input().split()) # L: 초밥 벨트 길이, Q: 명령 수
# belt = {}
# stand_by = {}
# time_cnt = 1
# for i in range(Q):
#     val = input().split()
#     if time_cnt != int(val[1]):
#         for _ in range((int(val[1])-time_cnt)%L):
#             belt = dict(((key+1)%L, value) for (key, value) in belt.items())
#     time_cnt = int(val[1])

#     if val[0] == '100': # 초밥 만들기
#         t, x, name = val[1:]
#         x = int(x)
#         try:
#             if name in list(zip(*belt[x]))[0]: # name 열 추출
#                 idx = list(zip(*belt[x]))[0].index(name)
#                 belt[x][idx][1]+=1
#             else:
#                 belt[x].append([name,1])
#         except:
#             belt[x]=[[name,1]]
#     elif val[0] == '200': # 손님 입장
#         t, x, name, n = val[1:]
#         t, x, n = int(t), int(x), int(n)
#         for _ in range(n): 
#             try:
#                 idx = list(zip(*belt[x]))[0].index(name) 
#                 belt[x][idx][1]-=1
#                 n-=1
#             except: # 먹을 초밥이 없는 경우
#                 stand_by[x]= [name, n]
#     elif val[0] == '300': # 사진 촬영
#         t = val[1:] 
#         belt, stand_by = check_waiting_customers(belt, stand_by)

#         if list(zip(*(itertools.chain(*belt.values())))):
#             res = list(zip(*(itertools.chain(*belt.values()))))[1]
#             print(len(stand_by), sum([x for x in res if x>0])) 
#         else:
#             print(len(stand_by), 0) 
            

#     belt, stand_by = check_waiting_customers(belt, stand_by)
#     print(belt, stand_by)


# ############################## [해설] ##########################33
# class Query:
#     def __init__(self, cmd, t, x, name, n):
#         self.cmd = cmd
#         self.t = t
#         self.x = x
#         self.name = name
#         self.n = n

# queries = []    # 명령
# names = set()   # 사람 목록
# p_queries = {}  # 사람별 초밥 명령
# entry_time = {} # 입장 시간
# position = {}   # 손님 위치
# exit_time = {}  # 퇴장 시간

# L, Q = map(int, input().split())
# for _ in range(Q):
#     command = input().split()
#     cmd, t, x, n = -1, -1, -1, -1
#     name = ""
#     cmd = int(command[0])
#     if cmd == 100:
#         t, x, name = command[1:]
#         t, x = map(int, [t, x])
#     elif cmd == 200:
#         t, x, name, n = command[1:]
#         t, x, n = map(int, [t, x, n])
#     else:
#         t = int(command[1])

#     queries.append(Query(cmd, t, x, name, n))

#     # 사람별 초밥 목록 관리
#     if cmd == 100:
#         if name not in p_queries:
#             p_queries[name] = []
#         p_queries[name].append(Query(cmd, t, x, name, n))
#     # 손님 입장 시간, 위치 관리
#     elif cmd == 200:
#         names.add(name)
#         entry_time[name] = t
#         position[name] = x

# # 각 사람마다 자신의 이름이 적힌 조합을 언제 먹게 되는지 계산하여 해당 정보를 기존 쿼리에 추가 (111번 쿼리)
# for name in names:
#     # 해당 사람의 퇴장 시간 : 마지막으로 먹는 초밥 시간 중 가장 늦은 시간
#     exit_time[name] = 0

#     for q in p_queries[name]:
#         # 초밥이 사람 등장 전 미리 주어진 상황
#         time_to_removed = 0
#         if q.t < entry_time[name]:
#             # entry_time때의 스시 위치
#             t_sushi_x = (q.x + (entry_time[name] - q.t)) % L
#             # 몇 초가 더 지나야 만나는지 계산
#             additional_time = (position[name] - t_sushi_x + L) % L  # 결과값이 항상 [0, L) 안에 들어오도록 (즉, 음수가 되지 않도록 하기 위해) L을 더함

#             time_to_removed = entry_time[name] + additional_time
#         # 초밥이 사람이 등장한 이후 주어진 상황
#         else:
#             # 몇 초가 더 지나야 만나는지 계산
#             additionl_time = (position[name] - q.x + L) % L
#             time_to_removed = q.t + additionl_time

#         # 초밥이 사라지는 시간 중 가장 늦은 시간을 업데이트
#         exit_time[name] = max(exit_time[name], time_to_removed)

#         # 초밥이 사라지는 111번 쿼리 추가
#         queries.append(Query(111, exit_time[name], -1, name, -1))

# # 사람마다 초밥을 마지막으로 먹은 시간 t를 계산하여 그 사람이 해당 t때 코드트리 오마카세를 떠났다는 Query 추가 (222번 쿼리)
# for name in names:
#     queries.append(Query(222, exit_time[name], -1, name, -1))

# # 전체 Query를 시간순으로 정렬하되 t가 일치한다면 문제 조건상 사진 촬영에 해당하는 100이 가장 늦게 나오도록 cmd순으로 오름차순 정렬
# # 이후 순서대로 보면서 사람, 초밥 수를 count하다가 300이 나오면 현재 사람, 초밥 수 출력
# queries.sort(key=lambda q: (q.t, q.cmd))

# people_num, sushi_num = 0, 0
# for i in range(len(queries)):
#     if queries[i].cmd == 100:   # 초밥 추가
#         sushi_num += 1
#     elif queries[i].cmd == 111:  # 초밥 제거
#         sushi_num -= 1
#     elif queries[i].cmd == 200:  # 사람 추가
#         people_num += 1
#     elif queries[i].cmd == 222:  # 사람 제거
#         people_num -= 1
#     else:  # 사진 촬영
#         print(people_num, sushi_num)

''' 
- 시간 복잡도 계산
쿼리 정렬 sort : O(NlogN) 
쿼리 처리 : O(N)
=> O(QlogQ)
- 메모리 복잡도 계산
=> O(Q)
'''