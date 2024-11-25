// Дан список из N (N≤2∗105) элементов,которые принимают целые значения от 0 до 100.
// Отсортируйте этот список в порядке неубывания элементов. Выведите полученный список.
// Решение оформите в виде функции CountSort(A), которая модифицирует передаваемый ей список.
// Примечание
// Сложность работы программы должна быть O(n). Использование встроенной сортировки(sort, sorted), алгоритмов сортировки пузырёк/quick sort/merge sort и других запрещено!

#include <iostream>
#include <vector>
using namespace std;
void CountSort(vector<int> & arr, int n){
    vector<int> counter(100);
    for (int i = 0; i < n; i++){
        counter[arr[i]] += 1;
    }
    arr.clear();
    for (int num = 0; num <= 100; num++){
        for (int i = 0; i < counter[num]; i++){
            arr.push_back(num);
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
    CountSort(arr, n);
    for (int i =0; i < n; i++){
        cout << arr[i] << " ";
    }
    return 0;
}
