#include <iostream>
#include <chrono>
using namespace std;
using namespace std::chrono;

int main() {
    int arr[100000] = {0};

    auto start = high_resolution_clock::now();
    volatile int sum = 0;
    for (int i = 0; i < 100000; ++i)
        sum += *arr;  // or *arr;
    auto end = high_resolution_clock::now();

    cout << "Time: " << duration_cast<nanoseconds>(end - start).count() << " ns\n";
    return 0;
}
