#include <iostream>
using namespace std;
int main()
{
    int n, k, cnt = 0;
    cin >> n;
    int a[n];
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];

        if (a[i] % 2 == 0)
        {
            k += a[i];
            cnt++;
        }
    }

    k = k / cnt;
    if (k > n)
    {
        k = k % n;
    }

    for (int i = n - k; i < n; i++)
    {
        cout << a[i] << " ";
    }
    for (int i = 0; i < n - k; i++)
    {
        cout << a[i] << " ";
    }
}