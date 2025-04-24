// 최대 증가 부분수열 (Longest Increasing Sequence) 길이 찾기
#include<bits/stdc++.h>
using namespace std;
int n, lis[1001], len, num;
int main(){
    scanf("%d", &n);
    for(int i=0; i<n; i++){
        scanf("%d", &num);

        auto lowerPos = lower_bound(lis, lis+len, num); // num보다 크거나 같은 첫번째 위치 리턴
        if(*lowerPos == 0) len++; // lis 배열에 num 보다 크거나 같은 값이 없으면 길이 카운트
        *lowerPos = num; // 없으면 추가, 있으면 대체

        cout << *lowerPos << '\n';
        for(int j=0; j<n; j++){
            printf("%d ", lis[j]);
        }
        printf("\n");
    }
    printf("%d", len);
    return 0;
}
/*
이 코드 단점 : 원본 배열이 회손됨

Input>
6
10 20 10 30 25 50
Output>
10
10 0 0 0 0 0
20
10 20 0 0 0 0
10
10 20 0 0 0 0
30
10 20 30 0 0 0
25
10 20 25 0 0 0
50
10 20 25 50 0 0
len : 4
*/