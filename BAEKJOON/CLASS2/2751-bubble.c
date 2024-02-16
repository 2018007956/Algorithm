//�������� �����ϱ�
//���� bubble sort ���� ���� �����. ����Լ� �̿�.
#include <stdio.h>
#include <stdlib.h> //malloc, free�Լ� ����� ��� ����
int ascending(int *arr,int n);
int main()
{
	int n; int *arr;
	scanf("%d", &n);
	arr = (int*)malloc(sizeof(int)*n);

	for ( int i = 0; i < n; i++ ) {
		scanf("%d", &arr[i]);
	}

	ascending(&arr[0],n); //arr ������ �ּҸ� ����! ù��° �ڸ��� ��������� �� ����� ����
	                            //�ƴϸ� �׳� ���� �̸��� arr�̷��� �־��൵ �ǰڴ�
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
			count++; //������ �Ϸ�� ���� ���� ����
		//	printf("count:%d \n", count);
		}
	}
	if ( count == n )
		return;
	ascending(&arr[0], n);
}
/* ����� ����� ��������, ���ؿ��� �ð��ʰ��� ���.
�˾ƺ��ϱ� ���� ������ �ּ� ��� �־��� �ð� ���⵵�� ��� O(N^2)�� ���� ����̱� ������
�ǿ������� �ʴٰ� �Ѵ�. O(N lg N)�� ���ĵ��� �˾ƺ��� �Ѵ�.
��ǥ������ ���� ����, �� ����(�̰� �����ؾ� �Ѵٴµ� ��?), �� ���� ���� �ִ�.
*/