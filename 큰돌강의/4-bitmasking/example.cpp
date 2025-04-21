// combi 안쓰고 for문 하나로 모든 경우의 수 표현
#include<bits/stdc++.h>
using namespace std;
const int n = 4;
int main(){
    string a[n] = {"사과", "딸기", "포도", "배"};
    for(int i=0; i<(1<<n); i++){
        string ret = "";
        cout << i << " : ";
        for(int j=0; j<n; j++){
            if(i&(1<<j)){ // 켜져있는 비트 체크
                ret += (a[j] + " ");
            }
        }
        cout << ret << '\n';
    }
    return 0;
}

// Tip) bufferflush 때문에 endl은 느려서 '\n' 개행문자로 하는게 좋음