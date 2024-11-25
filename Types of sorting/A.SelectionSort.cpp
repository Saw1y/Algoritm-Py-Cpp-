/*
Дан список целых чисел.Выведите все элементы этого списка в порядке невозрастания значений.Выведите новый список на экран.

Решите эту задачу при помощи алгоритма сортировки выбором.Решение оформите в виде функции SelectionSort(A).

В алгоритме сортировки выбором мы находим наибольший элемент в списке и ставим его на первое место, затем находим наибольший элемент из оставшихся и ставим его на второе место и т.д.
*/

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
