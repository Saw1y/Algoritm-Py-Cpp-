#include <iostream>
#include <vector>
using namespace std;

void insertion_sort(vector<int> & arr, int n){
    int key, j;
    for (int i = 0; i < n; i++){
        key = arr[i];
        j = i; 
        while (j >= 1 and arr[j - 1] > key){
            arr[j] = arr[j - 1];
            j -= 1;
        }
        arr[j] = key;
    }
    
}

int main(){
    int x, n;
    vector<int> arr;
    while (cin >> x){
        arr.push_back(x);
    }
    n = arr.size();
    insertion_sort(arr, n);
    for (int i = 0; i < n; i++){
        cout << arr[i] << " ";
    }
    return 0;
}
