#include <iostream>
#include <vector>
using namespace std;
void BubbleSort(vector<int> & arr, int n){
    bool swapped = false;
    for(int iter = 0; iter < n -1; iter++){
        swapped = false;
        for(int i = 0; i < n - iter - 1; i ++){
            if (arr[i] < arr[i+1]){
                swapped = true;
                swap(arr[i], arr[i+1]);
            }
        }
        if (swapped == false){
            break;
        }
    }
}

int main(){
    int x, n;
    vector<int> arr;
    while (cin >> x){
        arr.push_back(x);
    }
    n = arr.size();
    BubbleSort(arr, n);
    for (int i = 0; i < n; i++){
        cout << arr[i] << " ";
    }
    return 0;
}
