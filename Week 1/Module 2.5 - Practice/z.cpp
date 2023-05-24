/*
    ** Sujan Sarkar **
    Github: https://github.com/sujansarkar69
*/
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int k, s;
    cin >> k >> s;
    int res = 0;
    for (int i = 0; i <= k; i++)
    {
        for(int j = 0; j <= k; j++)
        {
            if(s - i - j >= 0 and s - i - j <= k)
            {
                res++;
            }
        }
    }
    cout << res << endl;
    return 0;
}