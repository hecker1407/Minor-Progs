#include<bits/stdc++.h>
using namespace std;
 int main()
 {
    vector<int> v;
    v.push_back(1);
    v.emplace_back(2);
    vector<int>::iterator it=v.begin();
    it ++;
    cout << *(it) << " ";
    array <int ,4> arr= {1,2,3,4};
    int ar[4]={1,2,3,4};
    cout <<  *ar;

 
  return 0;
 }
