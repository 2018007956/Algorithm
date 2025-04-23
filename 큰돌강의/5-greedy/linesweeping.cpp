/* 라인 스위핑
[예제] 큰돌이는 못말리는 화가야!!!
큰돌은 새로운 예술 프로젝트를 위해 도화지 위에 여러 선을 긋기로 했습니다.
그는 도화지의 특정 위치에서 다른 위치까지 여러 번 선을 그릴 수 있습니다.
하지만 선을 그을 때마다 이미 그어진 선 위에 다시 선을 그을 수 있으며, 이렇게 여러 번 그어진 부분은 한 번만 계산됩니다.

큰돌이 도화지에 그린 모든 선들의 총 길이를 구하는 프로그램을 작성하세요. 
여러 번 그어진 선이 있더라도, 겹쳐진 부분은 한 번만 계산해야 합니다.

첫째 줄에 선을 그은 횟수 N(1<=N<=1,000,000)이 주어지고 그 다음 N개의 줄에는 선을 그을 때 선택한
두 점의 위치 a, b(-1,000,000,000<=a<=b<=1,000,000,000)가 주어진다.

입력>
5
0 2
1 5
3 7
8 10
6 9
출력> 10
*/
#include<bits/stdc++.h>
using namespace std;
typedef pair<int, int> P;
P L[1000004];
int n, from, to, l, r, ret;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n;
    for(int i=0; i<n; i++){
        cin >> from >> to;
        L[i] = P(from, to);
    }
    sort(L, L+n); // 정렬
    l = L[0].first; r=L[0].second;
    for(int i=1; i<n; i++){
        if(r<L[i].first){
            ret += (r-l); // 이전 길이 저장
            // 구간 재정의
            l = L[i].first;
            r = L[i].second;
        }else if(L[i].first <= r && L[i].second >= r){
            r = L[i].second; // 오른쪽 끝 갱신
        }
    }
    ret += r - l;
}