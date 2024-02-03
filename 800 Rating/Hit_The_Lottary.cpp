#include <iostream>
using namespace std;

int minBils(){
    int n, count = 0;
    int array[] = {100, 20, 10, 5, 1};
    cin >> n;
    for (int i : array) {
        count += n / i;
        n %= i;
    }
    return count;
}

int main() {
    int count = minBils();
    cout << count << endl;
    return 0;
}
