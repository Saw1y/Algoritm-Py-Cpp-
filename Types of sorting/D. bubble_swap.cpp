/*
Определите, сколько обменов сделает алгоритм пузырьковой сортировки по возрастанию для данного массива.

Входные данные
На первой строке дано число N (1 ≤ N ≤ 1000) – количество элементов в массиве. На второй строке – сам массив. Гарантируется, что все элементы массива различны и не превышают по модулю 109.

Выходные данные
Выведите одно число – количество обменов пузырьковой сортировки.
*/

#include <iostream>
#include <vector>
using namespace std;

int number_swap(vector<int> & arr, int n){
    int num = 0;
    bool swapped;
    for (int i = 0; i < n - 1; i++){
        swapped = false;
        for (int j = 0; j < n - i - 1; j++){
            if (arr[j] > arr[j+1]){
                swapped = true;
                num++;
                swap(arr[j], arr[j+1]);
            }
        }
        if (swapped == false){
            break;
        }
    }
    return num;
}


int main(){
    int x, n, num;
    vector<int> arr;
    cin >> n;
    while (cin >> x){
        arr.push_back(x);
    }
    num = number_swap(arr, n);
    cout << num;
    return 0;
}
