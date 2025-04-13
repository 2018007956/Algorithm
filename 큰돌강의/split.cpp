#include<bits/stdc++.h>
using namespace std;

vector<string> split(string input, string delimiter){
    vector<string> result;
    auto end = 0; // find가 size-t 타입 형태를 반환
    while ((end=input.find(delimiter)) != string::npos) { // 찾을 수 없을 때까지 반복
        result.push_back(input.substr(0, end));
        input.erase(0, end + delimiter.size());
    }
    result.push_back(input);
    return result;
}

int main() {
    string str = "apple,banana,orange,grape";
    vector<string> fruits = split(str, ",");
    for (const string& fruit : fruits) {
        cout << fruit << " ";
    }
    return 0;
}