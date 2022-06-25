Algoritmo Compara_ulti_digito
	//Variables
	Definir num1, num2, ud1, ud2 Como Entero
	Escribir "Digite dos numero enteros"
	Leer  num1, num2
	
	si num1<0
		num1 = num1 * (-1)
	FinSi
	ud1 = num1 - num1 /10*10
	
	si num2 <0
		num2 = num2 * (-1)
	FinSi
	ud2= num2 - num2 /10*10
	
	si ud1 == ud2
		Escribir "El útlimo digito de un numero es igual al último digito del otro"
	SiNo
		Escribir "El último digito de un numero NO es igual al último digito del otro"
	FinSi
	
FinAlgoritmo
