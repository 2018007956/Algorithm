#include <bits/stdc++.h>
using namespace std;
vector<int> v {2, 2, 1, 1, 2, 2, 3, 3, 5, 6, 7, 8, 9};
int main(){
    sort(v.begin(), v.end());
    v.erase(unique(v.begin(), v.end()), v.end());
    for(int i : v) cout << i << " ";
    cout << '\n';
    return 0;
}
/*
1 2 3 5 6 7 8 9
*/

// 2)
vector<int> v;
int main(){
    for(int i=1; i<=5; i++){
        v.push_back(i);
        v.push_back(i); // 1 1 2 2 3 3 4 4 5 5
                        // 1 2 3 4 5 3 4 4 5 5 
    }
    for(int i: v) cout << i << " ";
    cout << '\n';
    // 중복되지 않은 요소로 채운 후, 그 다음 이터레이터를 반환한다.
    auto it = unique(v.begin(), v.end());
    cout << it - v.begin() << '\n'; // 5
    // 앞에서 부터 중복되지 않게 채운 후 나머지 요소들은 그대로 둔다.
    for(int i : v) cout << i << " ";
    cout << '\n';
    return 0;
}
/*
1 1 2 2 3 3 4 4 5 5 
5
1 2 3 4 5 3 4 4 5 5
*/

// 3)
map<int, int> mp;
int main(){
    vector<int> v{1, 1, 2, 2, 3, 3};
    for(int i : v){ // (int i=0; i<v.size(); i++)
        if(mp[i]){
            continue;
        }else{
            mp[i] = 1;
        }
    }
    vector<int> ret;
    for(auto it : mp){
        ret.push_back(it.first);
    }
    for(int i : ret) cout << i << '\n';
}