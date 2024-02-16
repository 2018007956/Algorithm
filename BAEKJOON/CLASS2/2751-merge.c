//merge sort로 똑같은 문제 다시 풀기
#include <stdio.h>
#include <stdlib.h>
void ms(int* arr, int n);
void mergeSort(int* arr, int* tmp, int start, int end);//c언어에선 함수이름 같으면 컴파일 에러
void merge(int* arr, int* tmp, int start, int mid, int end);
void printArray(int* arr, int n);
int main()
{
	int n; int *arr;
	scanf("%d", &n);
	arr = (int*)malloc(sizeof(int)*n);

	for ( int i = 0; i < n; i++ ) {
		scanf("%d", &arr[i]);
	}

	ms(arr,n);
	printArray(arr,n);
}
void ms(int* arr,int n)
{
	int* tmp = (int*)malloc(sizeof(int)*n);
	mergeSort(arr, tmp, 0, n - 1);
}
void mergeSort(int* arr, int* tmp, int start, int end)
{
	if ( start < end ) {
		int mid = (start + end) / 2;
		mergeSort(arr, tmp, start, mid);
		mergeSort(arr, tmp, mid + 1, end);
		merge(arr, tmp, start, mid, end);
	}
}
void merge(int* arr, int* tmp, int start, int mid, int end)
{
	for ( int i = start; i <= end; i++ )
		tmp[i] = arr[i];
	int part1 = start;
	int part2 = mid + 1;
	int index = start;
	while ( part1 <= mid && part2 <= end ) {
		if ( tmp[part1] <= tmp[part2] ) {
			arr[index] = tmp[part1];
			part1++;
		}
		else {
			arr[index] = tmp[part2];
			part2++;
		}
		index++;
	}
	for ( int i = 0; i <= mid - part1; i++ ) {
		arr[index + i] = tmp[part1 + i];
	}
}
void printArray(int* arr, int n)
{
	for ( int i = 0; i < n; i++ ) {
		printf("%d ", arr[i]);
	}
}
//통과!!