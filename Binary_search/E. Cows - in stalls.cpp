// На прямой расположены стойла, в которые необходимо расставить коров так, чтобы минимальное расcтояние между коровами было как можно больше.
// Входные данные
// В первой строке вводятся числа N (2<N<10001) – количество стойл и K
//  (1<K<N) – количество коров. Во второй строке задаются N
//  натуральных чисел в порядке возрастания – координаты стойл (координаты не превосходят 109)
// Выходные данные
// Выведите одно число – наибольшее возможное допустимое расстояние.

#include <iostream>
#include <vector>
using namespace std;
int check_val(int x, int k, vector<int> &arr){
    int cows = 1;
    int last_cow = arr[0];
    for(int i = 0; i < arr.size();i++){
        if (arr[i] - last_cow >= x){
            cows++;
            last_cow = arr[i];
        }
    }
    return cows >= k;
}

int main()
{
    int k;
    int n;
    cin >> n >> k;
    vector<int> arr;
    int x;
    while(cin >> x){
        arr.push_back(x);
    }
    int left = 1;
    int right = arr[n-1];
    while (right - left > 1)
    {
        int m = (right + left) / 2;
        if (check_val(m, k, arr)){
            left = m;
        }
        else{
            right = m;
        }
    }
    cout << left;
    return 0;
}
