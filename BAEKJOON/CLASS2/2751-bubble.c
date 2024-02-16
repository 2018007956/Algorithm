//오름차순 정렬하기
//나는 bubble sort 정렬 개념 사용함. 재귀함수 이용.
#include <stdio.h>
#include <stdlib.h> //malloc, free함수 선언된 헤더 파일
int ascending(int *arr,int n);
int main()
{
	int n; int *arr;
	scanf("%d", &n);
	arr = (int*)malloc(sizeof(int)*n);

	for ( int i = 0; i < n; i++ ) {
		scanf("%d", &arr[i]);
	}

	ascending(&arr[0],n); //arr 변수의 주소를 전달! 첫번째 자리를 지정해줘야 값 제대로 들어가네
	                            //아니면 그냥 변수 이름만 arr이렇게 넣어줘도 되겠다
	for ( int i = 0; i < n; i++ ) {
		printf("%d ", arr[i]);
	}
	free(arr);
	return 0;
}

int temp=0, count=0;
int ascending(int* arr,int n)
{
	int i;
	/*for ( int i = 0; i < n; i++ ) {
		printf("--- %d\n", arr[i]);
	}*/
	for ( i = n - 1; i > 0; i-- ) {
	//	printf("i:%d\n", i);
		if ( arr[i] < arr[i - 1] ) {
			temp = arr[i];
			arr[i] = arr[i - 1];
			arr[i - 1] = temp;
	//		printf("check : %d %d %d\n",arr[0], arr[1],arr[2]);
		}


		if ( i == 1 ) {
			count++; //정렬이 완료된 숫자 개수 세기
		//	printf("count:%d \n", count);
		}
	}
	if ( count == n )
		return;
	ascending(&arr[0], n);
}
/* 결과는 제대로 나오지만, 백준에선 시간초과로 뜬다.
알아보니까 버블 정렬은 최선 평균 최악의 시간 복잡도가 모두 O(N^2)인 정렬 방법이기 때문에
실용적이지 않다고 한다. O(N lg N)인 정렬들을 알아봐야 한다.
대표적으로 병합 정렬, 퀵 정렬(이건 조심해야 한다는데 뭘?), 힙 정렬 등이 있다.
*/