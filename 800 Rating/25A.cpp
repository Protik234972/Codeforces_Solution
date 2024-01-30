#include <iostream>
#include <vector>
using namespace std;

int evenness(vector<int> li) 
{
    int even_count = 0, odd_count = 0, even = 0, odd = 0;
    for (int i : li) {
        if (i % 2 == 0) {
            even_count += 1;
            even += i;
        } else {
            odd_count += 1;
            odd += i;
        }
    }

    if (even_count == 1) {
        for (int i = 0; i < li.size(); i++) {
            if (li[i] == even) {
                return i + 1;
            }
        }
    } else {
        for (int i = 0; i < li.size(); i++) {
            if (li[i] == odd) {
                return i + 1;
            }
        }
    }
    return 0;
}

int main() {
    int n;
    cin >> n;
    vector<int> li;
    while (n > 0) {
        int s;
        cin >> s;
        li.push_back(s);
        n--;
    }
    cout << evenness(li) << endl;
    return 0;
}
