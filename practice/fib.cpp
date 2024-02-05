# include<iostream>
using namespace std;

int fib(int n,array[n]){
    if (array[n] > 0) return array[n];
    if (n == 1 || n == 0) return n;
    else 
        array[n]=fib(n-1,array)+ fib(n-2,array);
        return array[n];
}

int main(){
    cout<< fib(10);
    return 0;
}