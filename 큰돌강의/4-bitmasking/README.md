## 비트연산자 
### SHIFT (<<,>>)
- a << b = a * 2^b
- a >> b = (int) a * (1/2)^b

### XOR (^)
같은 걸 싫어해~ 하면서 false(0) 반환
- 0^0 = 0
- 0^1 = 1
- 1^0 = 1
- 1^1 = 0

### One's completion 1의 보수연산자 (~)
비트 반전시키는 연산자
- ~value = -(value+1)

## 비트연산자 활용법
아래 내용 암기 필요  
|내용|연산자|
|---|---|
|idx번째 비트끄기|S &= ~(1<<idx)|
|idx번째 비트 XOR 연산|S ^= (1<<idx)|
|최하위 켜져있는 비트 찾기|idx = (S&-S)|
|크기가 n인 집합의 모든 비트를 켜기|(1<<n)-1|
|idx번째 비트를 켜기|S \|= (1<<idx)|
|idx번째 비트가 켜져 있는지 확인하기|if(S&(1<<idx))|

## 비트마스킹의 한계
31까지의 경우의 수만을 표현할 수 있음  
=> 문제에서 주어진 n이 31이하고, 경우의 수를 판단하는 문제이면 비트마스킹 사용해 볼 수 있음