#include <bits/stdc++.h>
#include<fstream>
using namespace std;

vector<int> correc(vector<int> &ar,int p){
    int n=ar.size();
    if(ar[n-p]==0)
        ar[n-p]=1;
    else
        ar[n-p]=0;

    return ar;
}

bool fun(int n){
    if(n==0)
        return false;
    return ceil(log2(n))==floor(log2(n));
}

int det(vector<int> ar){
    int n=ar.size();
    int p1=0,p2=0,p4=0,p=0;

    p1=ar[n-1]^ar[0]^ar[2]^ar[4];
    p2=ar[n-2]^ar[0]^ar[1]^ar[4];
    p4=ar[n-4]^ar[0]^ar[1]^ar[2];
    p=p1+(p2*2)+(p4*4);
    if(p==0)
        return 0;

    else
        return p;

}

vector<int> Generate(vector<int> ar,string s){
    int n=ar.size(),j=0;
    for(int i=0;i<n;i++)
        {
        if(fun(n-i))
        {
            ar[i]=0;
        }
        else
        {
            ar[i]=s[j]-'0';
            j++;
        }
    }
    ar[n-1]=ar[0]^ar[2]^ar[4];
    ar[n-2]=ar[0]^ar[1]^ar[4];
    ar[n-4]=ar[0]^ar[1]^ar[2];
    return ar;
}

int main(){
   cout<<"Hamming code generator:-\n";
   string hc;

    ifstream messagefile("ham.txt");
    while(getline(messagefile,hc))
        messagefile>>hc;

    cout<<hc<<endl;

   int l=hc.length()-1,r=0;

   while(pow(2,r)<=(l+r+1))
    r++;

   vector<int> ar(l+r+1,0);
   ar=Generate(ar,hc);
   cout<<"the generated hamming code is:-\n";
   for(int i=0;i<ar.size();i++){
    cout<<ar[i]<<" ";
   }
   cout<<endl;
   vector<int> a;
   cout<<"please enter the recieved message\n";
   for(int i=0;i<7;i++){
    int x;
    cin>>x;
    a.push_back(x);
   }
   int p=det(a);
   if(p==0){
    cout<<"the is no error\n";
   }
   else{
    cout<<"---------------------\nthere is Error\n";
    cout<<"error is at position "<<7-p+1<<" from the start\n";
    a=correc(a,p);
    cout<<"\nthe corrected hamming code is:-\n";
    for(int i=0;i<7;i++){
        cout<<a[i]<<" ";
   }
   }
}
