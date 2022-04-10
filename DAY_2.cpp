// Online C++ compiler to run C++ program online
#include <iostream>
#include <sstream>
#include <vector>
using namespace std;

int main() {
    string s;
    getline(cin,s);
    stringstream ss(s);
    int data;
    vector<int>v;
    int p=1;
    while(ss>>data)
    {
        v.push_back(data);
    }
    int n=size(v);
    int arr[n];
    for(int i=0; i<n; i++)
    {
        p=p*v[i];
    }
    for(int i =0;i<n; i++)
    {
        arr[i]=p/v[i];
    }
    for(int i=0; i<n; i++)
    {
        cout<<arr[i]<<" ";
    }
    return 0;
}