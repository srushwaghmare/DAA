#include <iostream>
using namespace std;

int countZeroes(int arr[], int n) {
    
    int low = 0, high = n - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;

        
        if (arr[mid] == 0 && (mid == 0 || arr[mid - 1] == 1)) {
            return n - mid; 
        }
        
        else if (arr[mid] == 1) {
            low = mid + 1;
        }

        else {
            high = mid - 1;
        }
    }
    return 0; 
}

bool isValidArray(int arr[], int n) {

    bool zeroStarted = false;
    for (int i = 0; i < n; i++) {
        if (arr[i] == 0) {
            zeroStarted = true;
        } else if (arr[i] == 1 && zeroStarted) {
            return false; 
        }
    }
    return true;
}

int main() {
    int n;
    cout << "Enter the size of the array: ";
    cin >> n;

    int arr[n];
    cout << "Enter the elements of the array (only 1s followed by 0s): ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    if (!isValidArray(arr, n)) {
        cout << "Invalid input: Array must contain all 1s followed by all 0s." << endl;
    } else {
        int zeroCount = countZeroes(arr, n);
        cout << "Count of zeros is " << zeroCount << endl;
    }

    return 0;
}
