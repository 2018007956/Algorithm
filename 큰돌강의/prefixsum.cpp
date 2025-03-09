#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int a[100004], b, c, psum[100004], n, m;
int main(){
    ios_base::sync_with_studio(false); cin.tie(NULL); cout.tie(NULL);
    cin >> n>> m;
    for(int i=1; i<=n; i++){
        cin >> a[i];
        psum[i] = psum[i-1] + a[i];
    }
    for(int i=0; i<m; i++){
        cin >> b >> c;
        cout << psum[c] - psum[b-1] << '\n';
    }
    return 0;
}
/*
8 3
1 2 3 4 5 6 7 8
1 4 
1 5
3 5
*/