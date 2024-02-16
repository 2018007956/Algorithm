#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;
int isSmall(long long number, int len){
    vector<long long> realNum;
    int reverseNumber;
    for(int i = 1; i <= len; i++){
        int rnumber = number / 10^(i);
        realNum.push_back(rnumber);
        
    } 
}

int main(){    
    cin.tie(NULL);
	ios_base::sync_with_stdio(false);


    long long D[10];

    D[1] = 9;
    D[2] = 9;
    D[3] = 90;
    D[4] = 90;
    D[5] = 900;
    D[6] = 900;
    D[7] = 9000;
    D[8] = 9000;

    long long num1;
    cin >> num1;
    long long temp = num1;
    int len  = 0;
    
    while (temp != 0)
    {
        temp = temp/10;
        len++;
    }

    long long res = 0;
    
    for(int i = 1; i <= len-1; i++){
        res = res + D[i];
    }
    vector<long long> v1;
    if (len % 2 == 0)
    {


    }
    
    cout<<res;
}
