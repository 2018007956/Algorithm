#include<bits/stdc++.h>
using namespace std;

vector<string> split(const string& input, string delimiter){
    vector<string> result;
    auto start = 0;
    auto end = input.find(delimiter); // find가 size-t 타입 형태를 반환
    while (end != string::npos) { // 찾을 수 없을 때까지 반복
        result.push_back(input.substr(start, end-start));
        start = end + delimiter.size();
        end = input.find(delimiter, start);
    }
    result.push_back(input.substr(start));
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