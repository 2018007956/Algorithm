#include<bits/stdc++.h>
using namespace std;
int main(){
    // next_permutation은 오름차순을 기반으로 순열을 만든다
    vector<int> a = {2, 1, 3};
    sort(a.begin(), a.end());
    // int a[] = {1, 2, 3};
    do{
        for(int i:a) cout << i << " ";
        cout << '\n';
    // }while(next_permutation(&a[0], &a[0] + 3));
    // }while(next_permutation(a, a + 3));
    }while(next_permutation(a.begin(), a.end()));
}