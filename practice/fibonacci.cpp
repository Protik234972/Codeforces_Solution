# include <iostream>
using namespace std;

int main(){
    int f1 = 0, f2 = 1,n_f, n;
    cout<<"Enter number : " << endl;
    cin>>n;
    cout<< "Fibonacci sequence "<< n << "th Number"<<endl;
    cout<<f1<<endl;


    while (n--){
        cout<<f2<<endl;
        n_f = f1 + f2;
        f1 = f2;
        f2 = n_f;

    }

    return 0;
}