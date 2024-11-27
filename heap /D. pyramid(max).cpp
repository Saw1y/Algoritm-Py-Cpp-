// Пирамида (максимум)
// Напишите программу, которая будет обрабатывать последовательность запросов таких видов:

// CLEAR — сделать пирамиду пустой (если в пирамиде уже были какие-то элементы, удалить все). Действие происходит только с данными в памяти, на экран ничего не выводится.

// ADD n — добавить в пирамиду число n. Действие происходит только с данными в памяти, на экран ничего не выводится.

// EXTRACT — вынуть из пирамиды максимальное значение. Следует и изменить данные в памяти, и вывести на экран или найденное максимальное значение, или, если пирамида была пустой, слово "CANNOT" (большими буквами).

// Входные данные
// Во входных данных записано произвольную последовательность запросов CLEAR, ADD и EXTRACT — каждый в отдельной строке, согласно вышеописанному формату.

// Суммарное количество всех запросов не превышает 200000.

// Выходные данные
// Для каждого запроса типа EXTRACT выведите на стандартный выход (экран) его результат (в отдельной строке).

// Примечание
// Задачу следует решить двумя способами. Один — использовать стандартную реализацию пирамиды в STL; она называется priority_queue, для её использования необходимо подключить заголовочный файл queue. 
// Другой способ — реализовать пирамиду самому, использовать разрешено лишь некоторые из следующих заголовочных файлов: iostream, fstream, сstdio, stdio.h, string, string.h, vector.

#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Heap {
private:
    vector<int> heap;
    int size;

    void siftUp(int i) {
        while (i / 2 > 0 && heap[i] > heap[i / 2]) {
            swap(heap[i], heap[i / 2]);
            i = i / 2;
        }
    }

    void siftDown(int i) {
        while (i * 2 <= size) {
            int j = (i * 2 + 1 > size || heap[i * 2] > heap[i * 2 + 1]) ? i * 2 : i * 2 + 1;
            if (heap[i] < heap[j]) {
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
        size++;
        siftUp(size);
    }

    int extract() {
        if (size == 0) return -1;  // Возвращаем -1 для пустой кучи
        int maxVal = heap[1];
        heap[1] = heap[size];
        size--;
        heap.pop_back();
        siftDown(1);
        return maxVal;
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
