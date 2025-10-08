#include <iostream>
#include <vector>
using namespace std;



void selection_sort(vector<int> & arr, int n){
    for (int i= 0; i < n - 1; i++){
        int key = arr[i];
        int ind = i;
        for (int j = i + 1; j < n; j++){
            if (arr[j] > key){
                key = arr[j];
                ind = j;
            }
        }
        if (i != ind){
            swap(arr[i], arr[ind]);
        }
    }
}

int main() {
    int x, n;
    vector<int> arr;
    while (cin >> x){
        arr.push_back(x);
    }
    n = arr.size();
    selection_sort(arr, n);
    for (int i = 0; i < n; i++){
        cout << arr[i] << " ";
    }
    return 0;
}
