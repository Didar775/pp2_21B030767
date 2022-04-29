#include <iostream>
using namespace std;

int main(){
    int a[8][8] = {
                  {9, 3, 9, 2, 9, 0, 0, 0},
                  {4, 4, 2, 1, 3, 7, 2, 1},
                  {7, 3, 5, 4, 3, 4, 8, 2},
                  {0, 6, 3, 3, 8, 1, 4, 0},
                  {3, 3, 3, 3, 6, 4, 2, 5},
                  {8, 7, 9, 8, 5, 5, 5, 7},
                  {7, 2, 0, 0, 4, 3, 1, 8},
                  {3, 4, 7, 8, 8, 9, 3, 1} 
                  };
   
    for (int j = 0; j < 7; j++){
        int max = a[j][0];
        for (int i = 0; i < 7; i++){
            if (a[i][j] > max){
                max = a[j][i];
            }
        }
         cout<< max << endl;
    }

}
        

    