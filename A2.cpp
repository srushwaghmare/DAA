#include <bits/stdc++.h>
using namespace std;

int main() 
{ 
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;

    int A[n];
    cout << "Enter the elements of the array: ";
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }

    int j = 0;
    for (int i = 0; i < n; i++) { 
        if (A[i] != 0) { 
            swap(A[j], A[i]); // Partitioning the array 
            j++; 
        } 
    } 
    
    cout << "Array after moving zeroes to the end: ";
    for (int i = 0; i < n; i++) { 
        cout << A[i] << " "; // Print the array 
    } 

    return 0; 
}

