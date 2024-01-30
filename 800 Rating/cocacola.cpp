#include <bits/stdc++.h>
using namespace std;

void coca(int t)
{
    int m,n,k;
    cin >> m >> n >> k;
    if (n <= 0 || k <= 0) {
        cout << "Case " << t << ": Invalid Input\n";
        return;
    }
    if (m >= 0 && n * k<=m )
    {
        cout << "Case " << t << ": Yes\n";
    }
    else
    {
        cout << "Case " << t << ": No\n";
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t, count = 1;
    cin >> t;
    while (t--)
    {
        coca(count);
        count += 1;
    }
    return 0;
}
