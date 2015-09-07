#include <iostream>
#include <cstring>
//#include <sys/types.h>
#include <sys/socket.h> // сокеты, бинды, ...
#include <arpa/inet.h> //inet_addr
#include <unistd.h>


using std::cout;
using std::cin;
using std::getline;
using std::string;


// https://stackoverflow.com/questions/15712821/c-error-undefined-reference-to-classfunction раздельная компиляция



class mppp{
public:
	mppp(const char *ip_new, unsigned short int port = 0, int type = 2);
	void client();
	void server();
	void setip(string buffer);
	void setport(string buffer);
	void verify(); //проверка клиента сервером, что протокол совпадает
private:
	int ERROR();
	bool secondary;
	int sockit;
	struct sockaddr_in addr;
	unsigned short int check_port(string buffer); // переводит из строки в номер с проверкой на пригодность
	char ip[42];
	unsigned short int port;
	string buffer;
};


void mppp::client(){
	char buffer_new[2048];
	while(1){
		if(getline(cin, buffer) == nullptr) break;
		int len_buffer = buffer.length();
		if(2047 < len_buffer) len_buffer = 2048;
		for(int i=0; i < len_buffer; ++i) buffer_new[i] = buffer[i];
		sendto(sockit, buffer_new, len_buffer, 0, (struct sockaddr *)&addr, sizeof(addr));
		int n = recvfrom(sockit, buffer_new, 2047, 0, nullptr, nullptr);
		buffer_new[n] = '\0';
		fputs(buffer_new, stdout);
	}
}


void mppp::server(){
	struct sockaddr_in client_addr[1];
	if(bind(sockit, (struct sockaddr *)& addr, sizeof(addr)) < 0){
		//ERROR
		cout << "not Binded\n";
	}
	else cout << "Binded\n";
	char buffer_new[2048];
	
	while(1){
		socklen_t len = sizeof(client_addr);
		int n = recvfrom(sockit, buffer_new, 2047, 0, (sockaddr *)client_addr, &len);
		sendto(sockit, buffer_new, n, 0, (sockaddr *)client_addr, sizeof(client_addr));
		buffer_new[n] = '\0';
	}
}




unsigned short int mppp::check_port(string buffer){
	// добавить обработку шестнадцатеричных и восьмеричных чисел
	int number = 0;
	int len_buffer = buffer.length(); //чем метод size отличаеца от метода length?
	if(len_buffer > 5){
		cout << "Incorrect port\n";
		return 0;
	}
	for(int i=0; i < len_buffer; ++i){
		if(buffer[i] > 47 && buffer[i] < 58){
			number *= 10;
			number += buffer[i] - 48;
		}
		else{
			// Можно оставить без вывода ошибки, а проверять не вернулся ли 0 или сделать ввиде исключения
			cout << "Error. Port must be a number\n";
			return 0;
		}
	}
	if(number > 65535){
		// Можно оставить без вывода ошибки, а проверять не вернулся ли 0 или сделать ввиде исключения
		cout << "Error. Port must be a number in range 1024 - 65535\n";
		return 0;
	}
	return number;
}





mppp::mppp(const char *ip_new, unsigned short int port_new, int type){
	if(port_new == 0){
		cout << "Enter port number(1024 - 65535): ";
		cin >> buffer;
		port_new = check_port(buffer);
	}
	port = port_new;
	int len_ip = strlen(ip_new);
	/*
	if(len_ip < 15){
		cout << "Enter IP address: ";
		cout >> buffer;
		if((len_ip = strlen(buffer) < 15) || (len_ip < 42) || (len_ip > 42)){
			cout << "IP is incorrect\n";
			exit(0);
		}
	}
	*/
	for(int i = 0; i < len_ip; ++i) ip[i] = ip_new[i];
	if(type == 2){
		cout << "What type of object do you prefer server[0]/client[1](default server): ";
		cin >> type;
	}
	if(type == 1) secondary = true;
	else secondary = false;
	sockit = socket(AF_INET, SOCK_DGRAM, 0);
	if(sockit < 0){
		//ERROR
		cout << "bad socket\n";
	}
	addr.sin_family = AF_INET;
	addr.sin_port = htons(port);
	addr.sin_addr.s_addr=inet_addr(ip);
	
	if(secondary) client();
	else server();
	close(sockit);
}




void mppp::setip(string buffer){
	//cin >> buffer;
	//можно добавить обработку ipv6
	int len_buffer = buffer.length();
	if(len_buffer > 15 && len_buffer < 42){
		// Добавить ошибку ввиде исключения
		cout << "Error. Incorrect IP address\n";
		ip[0] = '\0';
		return;
	}
	for(int i =0; i < len_buffer; ++i) ip[i] = buffer[i];
}



void mppp::setport(string buffer){
	//cin >> buffer;
	port = check_port(buffer);
}

