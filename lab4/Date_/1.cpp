#include <iostream>
#include <cmath>
using namespace std;
int main(){
    int n,m; 
    int a[n];
    cin >> n >> m;
    m=abs(m);
    for(int i=0; i<n; i++){
        cin>>a[i];
    }
    for(int i=n-m; i<n; i++){
        cout<<a[i]<<" ";
    }
    for(int i=0;i<n-m; i++){
        cout<<a[i]<<" ";
    }




}