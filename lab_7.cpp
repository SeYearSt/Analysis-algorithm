#include <iostream>
#include <random>
#include <ctime>
#define RAND_LIMIT 10
//#include <vector>
using namespace std;

void init(int *arr, int n,bool input);
void output(int * arr, int n);
void PSORT(int L[], int root, int key, int n);
void SORT(int *arr, int N);


void main() {
	srand(time(0));

	int n;

	cout << "Enter size of array: ";

	cin >> n;

	int * arr = new int[n];

	cout << "Array init:\n";
	init(arr, n,false);

	cout << "A = ";
	output(arr, n);

	SORT(arr, n);

	system("pause");
}
void init(int *arr, int n,bool input) {
	
	if (input) {
		for (int i = 0; i < n; ++i) {
			cout << "A[" << i + 1 << "] = ";
			cin >> arr[i];
		}
	}
	else {
		for (int i = 0; i < n; ++i) {
			bool exist = false;

			int temp = rand() % RAND_LIMIT + 1;
			
			for (int j = 0; j < n; ++i) {
				if (arr[j] == temp) {
					exist
				}

			}
		}
	}
	}

void output(int * arr, int n) {
	for (int i = 0; i<n; ++i) {
		cout << arr[i] << " ";
	}
	cout << endl;
}
void PSORT(int L[], int root, int key, int n) {
	int v = root;
	/*output(L, n);*/
	while (true) {
		if (2 * v + 1 <= n - 1) {
			int LC = 2 * v + 1;
			if (LC < n - 1) {
				if (L[LC + 1] > L[LC]) {
					++LC;
					if (L[LC] > key) {
						L[v] = L[LC];
						v = LC;
					}
					else {
						L[v] = key;
						return;
					}
				}
				else if (L[LC] > key) {
					L[v] = L[LC];
					v = LC;
				}
				else {
					L[v] = key;
					return;
				}
			}
			else if (L[LC] > key) {
				L[v] = L[LC];
				v = LC;
			}
			else {
				L[v] = key;
				return;
			}
		}
		else {
			L[v] = key;
			return;
		}
	}
}

void SORT(int *arr, int N) {

	for (int i = N / 2 - 1; i >= 0; --i)
	{
		PSORT(arr, i, arr[i], N);
	}

	cout << "Created pyramid: ";
	output(arr, N);

	for (int i = N - 1; i >= 0; --i) {
		int max = arr[0];
		PSORT(arr, 0, arr[i], i);
		arr[i] = max;
	}

	cout << "Sorted pyramid: ";
	output(arr, N);
}
