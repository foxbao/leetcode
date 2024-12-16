#include <iostream>
using namespace std;

void bubbleSort(int array[], int n) {
    for(int i=0;i<n-1;i++){
        for (int j=0;j<n-i-1;j++){
            if(array[j]>array[j+1]){
                swap(array[j],array[j+1]);
            }
        }
    }
}

int main() {
    int array[] = {5, 3, 8, 6, 2};
    int n = sizeof(array) / sizeof(int);

    bubbleSort(array, n);

    for (auto i:array) {
        cout << i << " ";
    }

    return 0;
}
