#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int main(){
    
    cin.tie(NULL);
	ios_base::sync_with_stdio(false);

    int ph = 0,pg = 0;
    string s1;
    getline(cin,s1);

    for(char c : s1){
        if(c == 'A'){
            ph++; pg++;
        }
        else if(c == 'H' || c == 'P' || c == 'Y'){
            ph++;
        }
        else if(c == 'S' || c =='D'){
            pg++;
        }
    }
    if(ph == 0 && pg == 0){
        cout<<"50.00"<<"\n";
    }
    else{
        double res;
        res = (double)ph/(ph+pg);
        res = res*100;
        printf("%.2f",res);
    }
}