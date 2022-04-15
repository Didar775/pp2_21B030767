#include <iostream>
using namespace std;
int main()
{
    int n;
    cin >> n;
    int a[n][n];
    int b[n][n];
    int mx = -1e9, max1;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> a[i][j];
            max1 = max(a[i][j], mx);
        }
    }
    // for (int i = 0; i < n; i++)
    // {
    //     for (int j = 0; j < n; j++)
    //     {
    //         if(a[i][j] == max1){
    //             int k=a[0][0];
    //             b[0][0] == max1;
    //             b[i][j] == k;
    //         }else{
    //         b[i][j] = a[i][j];
    //         }
    //     }
    // }
    int pos_i, pos_j;
    int cnt=0;
    int k = 0;
    while (n  != 0)
    {
        for (int i = 0; i < n; i++)                                     // 8 5 10 6    10 5 8 6 
        {                                                               // 5 1 3 2     5 1 3 2
                                                                        // 0 3 6 9     0 3 6 9
                                                                      // 9 6 3 8     9 6 3 8
            for (int j = 0; j < n; j++)
            {
               if(a[i][j] > mx){
                   if(max1 == a[i][j]){
                       cnt++;
                   }else{
                       mx = a[i][j];
                       pos_i = i;
                       pos_j = j;
                   }
               }
                
            }
          
        }
        int temp = b[k][k];
        b[k][k] = mx;
        b[pos_i][pos_j] = temp;
        k++;
        n--;
     
        
    }

    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cout<<b[i][j]<<" ";
        }
        cout<<endl;
    }
}
    
