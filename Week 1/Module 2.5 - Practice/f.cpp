/*
    ** Sujan Sarkar **
    Github: https://github.com/sujansarkar69
*/
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int x, n;
    cin >> x >> n;
    long long result = 0;
    for (int i = 2; i <= n; i+= 2)
    {
        result += pow(x, i);
    }
    cout << result << endl;
    
    return 0;
}