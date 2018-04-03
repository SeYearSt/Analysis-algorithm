#include <iostream>
//#include <random>
//#include <ctime>
//#include <vector>
using namespace std;

void init(int *arr, int n);
void output(int * arr, int n);
void PSORT(int L[], int root, int key, int n);

//output(arr, N);


void SORT(int *arr,int N) {
	
	for (int i = N / 2 -1; i >= 0; --i)
	{
		PSORT(arr, i, arr[i], N);
	}

	for (int i = N - 1; i >= 0; --i) {
		int max = arr[0];
		PSORT(arr, 0, arr[i], i - 1);
		arr[i] = max;
	}
}

void main() {
	int const n = 10;
	int arr[n] = {9,8,7,6,5,4,3,2,1,0};

	output(arr, n);
	SORT(arr, n);
	output(arr, n);
	system("pause");
}
void init(int *arr, int n) {
	//srand(time(0));
	for (int i = 0; i < n; ++i) {
		arr[i] = 2 * i +1;
	}
}
void output(int * arr, int n) {
	for(int i=0;i<n;++i){
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

	//
	//	
	//		else if (L[LC] > key) {
	//			L[v] = L[LC];
	//			v = LC;
	//		}
	//		else {
	//			L[v] = key;
	//			return;
	//		}
	//	}

	//	

	//}
	//