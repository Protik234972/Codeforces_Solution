#include<bits/stdc++.h>
using namespace std;

#define int long long
int32_t main(){

	int tt;	cin >> tt;
	while(tt--){
		int x,n;	cin >> x >> n;
		int p = -1;
		for(int i=1;i*i<=x;i++){
			if(x%i == 0 && x/i >= n) p=max(p,i);
            if(x%i == 0 && i >= n) p=max(p,x/i);
		}
		cout << p << '\n';
	}
}