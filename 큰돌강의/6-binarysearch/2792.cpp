#include<bits/stdc++.h>
using namespace std;
int n, m, bosuk[300004], ret=1e18;
bool check(int mid){
    int num = 0;
    for(int i=0; i<m; i++){
        num += bosuk[i] / mid;
        if(bosuk[i]%mid) num++;
    }
    return num <= n;
}
int main(){
    cin >> n >> m;
    int left = 1, right = 0, mid;
    for(int i=0; i<m; i++){
        cin >> bosuk[i];
        right = max(right, bosuk[i]);
    }
    while(left <= right){
        mid = (left+right)/2;
        if(check(mid)){
            ret = min(ret, mid);
            right = mid - 1;
        }else left = mid + 1;        
    }
    cout << ret << "\n";
}