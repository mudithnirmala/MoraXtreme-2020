#include<iostream>
#include <fstream>

using namespace std;
int aCount[100000][26];

int main(){

  //for(int i=0;t<27;t++){
    //string inf_name="input" +(t<10:"0":"");
    //string inf_name="output" +(t<10:"0":"");

//    ifstream cin(inf_name);
  //  ofstream fout(outf_name);

    string A,B;

    cin>>A>>B;
    int N=A.size();
    int M=B.size();

    long long ans=0;

    for(int i=0;i<N;i++) for(int j=0;j<26;j++) aCount[i][j]=0;

    aCount[0][A[0]-'A']=1;
    for(int i=1;i<N;i++){
        for(int j=0;j<26;j++)  aCount[i][j]=aCount[i-1][j];
        aCount[i][A[i]-'A']++;
    }

    for(int j=0;j<M;j++){
        int x = (aCount[N-M+j][B[j]-'A'])-(j>0? aCount[j-1][B[j]-'A']:0);
        ans+=x;
        cout<<x<<endl;
    }

    cout<<ans<<endl;
    cout<<ans<<endl;
 // }
    return 0;

}
