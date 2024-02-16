#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string>
#define MAX 2000000001

using namespace std;
int resList[100][100];

int main(){
    
    cin.tie(NULL);
	ios_base::sync_with_stdio(false);

    vector<pair<int,int>> sList;
    sList.push_back(make_pair(0,0));//index 0 .

    int n;
    cin>>n;

    for(int i = 1; i <=n; i++){
        pair<int,int> tmp;
        cin>>tmp.first>>tmp.second;
        sList.push_back(tmp);
    }

    int result = -1;
    for(int i = 1; i < sList.size() - 1; i++){
        resList[sList[i].first][sList[i].second]++;
        if(result <= resList[sList[i].first][sList[i].second]){
            result = resList[sList[i].first][sList[i].second];
        }
        for(int j = i+1; j < sList.size(); j++){
            int x = (sList[i].first + sList[j].first)/2;
            int y = (sList[i].second + sList[j].second)/2;
            resList[x][y]++;
            resList[x][y]++;
            if(result <= resList[x][y]){
                result = resList[x][y];
            }
        }
    }
    cout<<result<<"\n";
    
}