/*
    ** Sujan Sarkar **
    Github: https://github.com/sujansarkar69
*/
#include <bits/stdc++.h>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    int ans = 0, minn = INT_MAX;

    for (int i = 0; i < n; i++)
    {
        ans = 0;
        while (arr[i] % 2 == 0)
        {
            ans++;
            arr[i] /= 2;
        }
        minn = min(ans, minn);
    }

    cout << minn << endl;

    return 0;
}