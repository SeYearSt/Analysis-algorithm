#include <iostream>
#include <ctime>
#include <iomanip>
#include <conio.h>
using namespace std;

void insertionSort(int *, int); 

int main(int argc, char* argv[])
{
	srand(time(NULL));
	cout << "Input size of array: ";
	int size_array; 
	cin >> size_array;

	int *sorted_array = new int[size_array]; 
	cout << "A = ";
	for (int j = 0; j < size_array; j++)
	{
		sorted_array[j] = rand() % 100; 
		cout << sorted_array[j] << "  ";
	}
	cout << "\n";

	insertionSort(sorted_array, size_array); 
	cout << "A = ";
	for (int j = 0; j < size_array; j++)
	{
		cout << sorted_array[j] << "  "; 
	}
	cout << "\n";
	delete[] sorted_array; 
	cout << "\nPress any key...\n";
	while (!_kbhit());
	return 0;
}

void insertionSort(int *arrayPtr, int length) 
{
	int temp,i; 
	for (int j = 1; j < length; j++)
	{
		temp = arrayPtr[j]; 
		i = j - 1; 
		while (i >= 0 && arrayPtr[i] > temp) 
		{
			arrayPtr[i + 1] = arrayPtr[i]; 
			arrayPtr[i] = temp;
			i--;
		}
	}

}