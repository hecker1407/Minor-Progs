#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    int m;
    int a;
    int b;
    cout << "Enter The sizes of the Matrices";
    cin >> m >> n >> a >> b;
    if(m!=a)
    cout << "Matrices are not Compatible for Multiplication";
    else{
        int A[n][m];
        int B[a][b];
        int M[n][b];
       for(int i=0;i<n;i++){
            for(int j=0;j<b;j++){
                for(int k=0;k<m;k++){
                    M[i][j]+=A[i][k]*B[k][j];
                }
                cout << M[i][j] << " ";
            }
            cout << endl ;
        }
    }
 return 0;
}




