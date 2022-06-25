#include <iostream>
#include <stdlib.h>
using namespace std;

class Cliente {
 	private:
 		string cedula;
 		string nombre;
 		string telefono;
 	public:
 		Cliente(string,string,string);
 		void comprar();
 		void alquilar();								
};

Cliente::Cliente(string laCedula, string elNombre, string elTelefono){
	cedula=laCedula;
	nombre=elNombre;
	telefono=elTelefono;	
}

void Cliente::comprar(){
	cout<< "El cliente "<<nombre<<" ha comprado un videojuego "<<endl;
}

void Cliente::alquilar(){
	cout<<" Videojuego alquilado a "<<nombre<<" con documento "<<cedula<<endl;
	cout<<" En caso de demoras en la entrega llamar al "<<telefono<<endl;
}

int main(){
	Cliente cliente1=Cliente("14324465"," Luis Hurtado "," 3182342344");
	Cliente cliente2=Cliente("2345565 "," Camilo Zabala "," 2516723");
	
	cliente1.alquilar();
	cliente2.comprar();
	
	system("pause");
	return 0;
}



