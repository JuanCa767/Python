#include <iostream.h>
void main()
	int num;
	cin >> num;
	if (num < 0)
		cout<<"El numero debe ser positivo";
	else
		if(num/2*2==num)
			cout<< "El numero es par ";
		else
			cout<<"El numero es Impar";
