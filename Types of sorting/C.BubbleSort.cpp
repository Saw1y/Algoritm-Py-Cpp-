/*
Дан список целых чисел. Отсортируйте его в порядке невозрастания значений. Выведите полученный список на экран.

Решите эту задачу при помощи алгоритма пузырьковой сортировки.Решение оформите в виде функции BubbleSort(A).

В алгоритме пузырьковой сортировки осуществляется проход по списку от начала к концу, и если два соседних элемента списка стоят в неверном порядке, то они переставляются в правильном порядке.
В результате минимальный элемент массива окажется на последнем месте. Повторим эту процедуру еще несколько раз, чтобы поставить все элементы на свои места.

Вспомогательным списком пользоваться нельзя.
*/

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
