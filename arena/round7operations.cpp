#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int count = 0;
    string s;
    cin >> s;
    for(size_t i=0; i < s.size()-1; ++i){
        if(s[i] != s[i+1]) count++;
    }
    cout << (count+1)/2 << "\n";
}
