# include <iostream>
using namespace std;

int main(){
    int t; cin>>t;
    while (t--){
        int n,k; cin>>n>>k;
        
        if (k<n){
            cout<<k<<endl;
            continue;
        }
        int ans = k +(k/(n-1));
        if (ans % n == 0) ans--;
        cout<<ans<<endl;
    }
    return 0;
}