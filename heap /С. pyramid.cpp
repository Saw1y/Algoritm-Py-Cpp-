// Пирамида (минимум)
// Задача отличается от задачи «Пирамида (максимум)» исключительно тем, что надо извлекать не максимум, а минимум.

// Напишите программу, которая будет обрабатывать последовательность запросов таких видов:

// CLEAR — сделать пирамиду пустой (если в пирамиде уже были какие-то элементы, удалить все). Действие происходит только с данными в памяти, на экран ничего не выводится.

// ADD n — добавить в пирамиду число n. Действие происходит только с данными в памяти, на экран ничего не выводится.

// EXTRACT — вынуть из пирамиды минимальное значение. Следует и изменить данные в памяти, и вывести на экран или найденное минимальное значение, или, если пирамида была пустой, слово "CANNOT" (большими буквами).

// Входные данные
// Во входных данных записано произвольную последовательность запросов CLEAR, ADD и EXTRACT — каждый в отдельной строке, согласно вышеописанному формату.

// Суммарное количество всех запросов не превышает 200000.

// Выходные данные
// Для каждого запроса типа EXTRACT выведите на стандартный выход (экран) его результат (в отдельной строке).

// Примечание
// Собственно, это тот случай, когда, не имея под руками справочных материалов, легче реализовать структуру данных самому, чем добиться от стандартной реализации, чтобы она заработала так как надо... Но это все же возможно. Пирамиду с максимумом в корне объявляют просто как

// priority_queue<T> the_heap; а пирамиду с минимумом в корне — как

// priority_queue<T, vector<T>, greater<T> > the_heap; При этом, второй параметр (vector<T>) задает тип контейнера, в котором будет храниться пирамида (и менять вектор на что бы ни было другое практически никогда не бывает целесообразно), а третий параметр (который, когда ничего не сказано, равен less<T>) задает, какую операцию следует использовать при проверке основного свойства пирамиды в качестве операции «меньше». Когда на место операции «меньше» подставляется операция «больше» — как раз и получается, что упорядоченность пирамиды заменяется на противоположную.

// Разумеется, вместо T следует написать тип элементов, которые будем хранить в пирамиде.

#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Heap {
private:
    vector<int> heap;
    int size;

    void siftUp(int i) {
        while (i / 2 > 0 and heap[i] < heap[i / 2]) {
            swap(heap[i], heap[i / 2]);
            i = i / 2;
        }
    }

    void siftDown(int i) {
        while (i * 2 <= size) {
            int j = (i * 2 + 1 > size or heap[i * 2] < heap[i * 2 + 1]) ? i * 2 : i * 2 + 1;
            if (heap[i] > heap[j]) {
                swap(heap[i], heap[j]);
                i = j;
            } else break;
        }
    }

public:
    Heap() : size(0) {
        heap.push_back(0);  
    }

    void clear() {
        heap.clear(); 
    	heap.push_back(0);
        size = 0;
    }

    void add(int k) {
        heap.push_back(k);
        size = size + 1;
        siftUp(size);
    }

    int extract() {
        if (size == 0) return -1; 
        int minVal = heap[1];
        heap[1] = heap[size];
        size = size - 1;
        heap.pop_back();
        siftDown(1);
        return minVal;
    }
};

int main() {
    Heap heap;
    string command;

    while (cin >> command) {
        if (command == "CLEAR") {
            heap.clear();
        } else if (command == "ADD") {
            int n;
            cin >> n;
            heap.add(n);
        } else if (command == "EXTRACT") {
            int result = heap.extract();
            if (result == -1) {
                cout << "CANNOT" << endl;
            } else {
                cout << result << endl;
            }
        }
    }

    return 0;
}
