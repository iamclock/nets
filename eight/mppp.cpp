#include <iostream>
#include <cstring>
//#include <sys/types.h>
#include <sys/socket.h> // сокеты, бинды, ...
#include <arpa/inet.h> //inet_addr
#include <unistd.h>



// для пуша


using std::cout;
using std::cin;
using std::getline;
using std::string;


// https://stackoverflow.com/questions/15712821/c-error-undefined-reference-to-classfunction раздельная компиляция



class mppp{
public:
	mppp(string ip_new, unsigned short int port = 0, int type = 2);
	void client();
	void server();
	void setip(string buffer);
	void setport(string buffer);
	void verify(); //проверка клиента сервером, что протокол совпадает
private:
	int ERROR();
	bool secondary;
	int sockit;
	struct sockaddr_in addr, addr2;
	unsigned short int check_port(string buffer); // переводит из строки в номер с проверкой на пригодность
	char ip[42];
	unsigned short int port;
	string buffer;
};


mppp::mppp(string ip_new, unsigned short int port_new, int type){
	if(port_new == 0){
		cout << "Enter port number(1024 - 65535): ";
		cin >> buffer;
		port_new = check_port(buffer);
	}
	port = port_new;
	//int len_ip = ip_new.length;
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
	//for(int i = 0; i < len_ip; ++i) ip[i] = ip_new[i];
	//cout << ip_new << '\n' << ip_new.length();
	setip(ip_new);
	
	if(type == 2){
		type = false;
		// Проверить, что будет с type, если ввести не 0 и 1
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
	bzero(&addr, sizeof(addr));
	addr.sin_family = AF_INET;
	addr.sin_port = htons(port);
	if(secondary) client();
	else server();
	close(sockit);
}



void mppp::client(){
	char buffer_new[2048];
	int n;
	//cout << ip;
	addr.sin_addr.s_addr=inet_addr(ip);
	while(1){
		cout << "Enter something: ";
		if(getline(cin, buffer) == nullptr) break;
		int len_buffer = buffer.length();
		if(2047 < len_buffer) len_buffer = 2048;
		for(int i=0; i < len_buffer; ++i) buffer_new[i] = buffer[i];
		n = sendto(sockit, buffer_new, len_buffer, 0, (struct sockaddr*)&addr, sizeof(addr));
		cout << "Send: " << n << '\n';
		n = recvfrom(sockit, buffer_new, 2047, 0, (struct sockaddr*)&addr,
 (socklen_t*)sizeof(addr));
		cout << "Received: " << n << '\n';
		//buffer_new[n] = '\0';
	}
}


void mppp::server(){
	char buffer_new[2048];
	int n;
	addr.sin_addr.s_addr=INADDR_ANY;
	if(bind(sockit, (struct sockaddr *)& addr, sizeof(addr)) < 0){
		//ERROR
		cout << "not Binded\n";
	}
	else cout << "Binded\n";
	
	socklen_t len = sizeof(addr2);
	while(1){
		n = recvfrom(sockit, buffer_new, 2047, 0, (struct sockaddr*)&addr2, &len);
		cout << "Received: " << n << '\n';
		n = sendto(sockit, buffer_new, n, 0, (struct sockaddr*)&addr2, len);
		cout << "Send: " << n << '\n';
		buffer_new[n] = '\0';
		cout << "Received string: " << buffer_new << '\n';
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
	for(int i = 0; i <= len_buffer; ++i){
		// Подумать над условием, возможно можно сделать проще
		// Например в слуае, когда символ лежит в диапазоне то второе условие не проверять
		if((buffer[i] < 48 || buffer[i] > 58) && (buffer[i] != '.' && buffer[i] != '\0')){
			cout << "Error. Incorrect IP address\n";
			ip[0] = '\0';
			return;
		}
		ip[i] = buffer[i];
	}
}



void mppp::setport(string buffer){
	//cin >> buffer;
	port = check_port(buffer);
}

