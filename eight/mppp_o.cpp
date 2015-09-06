#include <sys/socket.h>
//#include <cstdlib>
#include <iostream>


using std::cout;
using std::cin;


class mppp{
	
	void mppp();
	void object();
	void client(int socket);
	void server(int socket);
	void setip();
	void setport();
	void verify(); //проверка клиента сервером, что протокол совпадает
	
private:
	struct sockaddr_in sin//{
// 		sin_family = AF_INET;
// 		sin_addr = 0;
// 		sin_port = 0;
// 	}
	
};



void mppp::mppp(){
	int socket;
	if (socket = socket(, , ) < 0){
		cout << "Ошибка в сокете\n"
		return
	}
	if (bind(, ,) < 0){
		cout << "Ошибка в бинде\n"
		return
	}
	cout << "Сервер[0]/Клиент[1]: ";
	cin >> socket;
	switch(socket){
	 case 0:{
		
		
		
	 }
	 case 1:{
		
		
		
	 }
	 default:{
		// Nothing вернуть ошибку
	 }
	}
	
	
	
}


void mppp::client(int socket){
	socket();
	bind();
	listen();
	accept();
	
}



void mppp::server(int socket){
	socket();
	bind();
	listen();
	accept();
	
}



void mppp::setip(/*char ip*/){
// 	sin.
}



void mppp::setport(/*unsigned short int port*/){
// 	sin.sin_port = htons(port)
}