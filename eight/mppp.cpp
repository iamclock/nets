#include <iostream>
#include <cstring>
//#include <sys/types.h>
#include <sys/socket.h> // сокеты, бинды, ...
#include <arpa/inet.h> //inet_addr
#include <unistd.h>
#include <ctime>
#include <cerrno>
#include <netdb.h>
#define TIMEOUT_MS 100
#define SERVER 0
#define CLIENT 1


using std::cout;
using std::cin;
using std::getline;
using std::string;

// https://stackoverflow.com/questions/15712821/c-error-undefined-reference-to-classfunction раздельная компиляция
// http://www.cyberforum.ru/post5972945.html
// http://www.cyberforum.ru/cpp-networks/thread1125443.html



class mppp{
public:
	/*
	typedef struct icmp_header{
		unsigned char ucType;
		unsigned char ucCode;
		unsigned short int usChecksum;
		unsigned short int usID;
		unsigned short int usSeq;
		char cData; // добавляет 2 байта
	}ICMPHeader;
	*/
	/*
	typedef struct ip_header{
		unsigned char verhlen;
		unsigned char tos:6;
		unsigned char additional:2;
		unsigned short totallent;
		unsigned short id;  
		unsigned short offset;
		unsigned char ttl;
		unsigned char proto;
		unsigned short checksum;
		unsigned int source;
		unsigned int destination;
	}IPHeader;
	*/
	mppp(unsigned short int port = 0, int type = 2, char *ip_new = nullptr);
	void client();
	void server();
	void setip(char *ip);
	void setport(string buffer);
	//void verify(); //проверка клиента сервером, что протокол совпадает
	//unsigned short int checkSUM(unsigned short int *, int);
private:
	int ERROR();
	// функция формирует пакет с эхо
	//void packetForm(char *); //наверное лучше сделать (char *), но тогда придёца удалять внутри функции client()
	bool secondary;
	int sockit, packetSize;
	struct sockaddr_in addr, addr2;
	unsigned short int check_port(string buffer); // переводит из строки в номер с проверкой на пригодность
// 	char ip[42];
	unsigned short int port;
	string buffer;
};

/*
unsigned short int mppp::checkSUM(unsigned short int *point, int size){
	
}
*/




mppp::mppp(unsigned short int port_new, int type, char *ip_new){
	if(port_new == 0){
		do{
			cout << "Enter port number(1024 - 65535): ";
			getline(cin, buffer);
			port_new = check_port(buffer);
		}while(port_new < 1024);
// 		cin >> buffer;
// 		port_new = check_port(buffer);
	}
	port = port_new;
	cout << port << '\n';
	addr.sin_port = htons(port);
	
	while(type == 2){
		type = 0;
		static char type_new = '0';
		cout << "What type of object do you prefer server[0]/client[1](default server): ";
		type_new = cin.get();
		if(type_new == '1') type = 1;
		else{
			if(type_new != '0' && type_new != '\n'){
				type = 2;
				cout << "Incorrect value. Try again\n";
				while( type_new = cin.get() != '\n' );
			}
		}
	}
	secondary = (bool)type;
	
	
	if(ip_new) setip(ip_new);
	else if(secondary){
		cout << "ERROR: IP address required\n";
		exit(0);
		// можно добавить предложение о вводе
	}
	
	sockit = socket(AF_INET, SOCK_DGRAM, 0);
	if(sockit < 0){
		perror("socket creating");
		exit(0);
	}
	addr.sin_family = AF_INET;
	if(secondary) client();
	else server();
	close(sockit);
}

/*
void mppp::packetForm(char *packet){
	
}
*/



void mppp::client(){
	
	char buffer_new[2048];
	int n, garanty;// size = sizeof(ICMPHeader)/*+sizeof(IPHeader)*/+32;
	//char *packet = new char[size];
	//packetForm(packet);
	//cout << packet << '\n';
	
	struct timeval timeout;
	timeout.tv_sec = 1;
	timeout.tv_usec = 0;
	setsockopt(sockit, SOL_SOCKET, SO_RCVTIMEO, &timeout, sizeof(timeout));
	socklen_t len = sizeof(struct sockaddr_in);
	while(1){
		garanty = 0;
		cout << "Enter something: ";
		if(getline(cin, buffer) == nullptr) break; // добавить обработку строки на выход
		int len_buffer = buffer.length();
		if(2047 < len_buffer) len_buffer = 2048;
		for(int i=0; i < len_buffer; ++i) buffer_new[i] = buffer[i];
		
		do{
			++garanty;
			n = sendto(sockit, buffer_new, len_buffer, 0, (struct sockaddr *)&addr, len);
			cout << "Send: " << n << '\n';
			if(garanty > 4){
				// проверка, что пакет дошёл
				cout << "Server is unreacheable\n";
				break;
			}
		n = recvfrom(sockit, buffer_new, 2047, 0, (struct sockaddr *)&addr, &len);
		}while( n < 0);
		if(garanty < 4){
			cout << "Received: " << n << '\n';
		}
		//buffer_new[n] = '\0';
	}
	//delete []packet;
}


void mppp::server(){
	char buffer_new[2048];
	int n;
	addr.sin_addr.s_addr=INADDR_ANY;
	if(bind(sockit, (struct sockaddr *)& addr, sizeof(addr)) < 0){
		perror("binding");
		exit(0);
	}
	else cout << "Binded\n";
	
	socklen_t len = sizeof(struct sockaddr_in);
	while(1){
		n = recvfrom(sockit, buffer_new, 2047, 0, (struct sockaddr *)&addr2, &len);
		cout << "Received: " << n << '\n';
		
		n = sendto(sockit, buffer_new, n, 0, (struct sockaddr *)&addr2, len);
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




void mppp::setip(char *ip){
	struct hostent *host;
	
	if (inet_addr(ip) != INADDR_NONE)
		addr.sin_addr.s_addr = inet_addr(ip);
	else{
		if ( host = gethostbyname(ip) )
			addr.sin_addr = *(struct in_addr *) host->h_addr_list[0];
		else{
			herror("Incorrect address");
		}
	}
}













/*
void setip(string buffer){
	//cin >> buffer;
	//можно добавить обработку ipv6
	int len_buffer = buffer.length();
	if(len_buffer > 15 && len_buffer < 42){
		// Добавить ошибку ввиде исключения
		cout << "Error. Incorrect IP address\n";
		ip[0] = '\0';
		return;
	}
	if(buffer == "localhost") buffer = "127.0.0.1"; // немного костылей
	for(int i = 0; i <= len_buffer; ++i){
		// Подумать над условием, возможно можно сделать проще
		// Например в случае, когда символ лежит в диапазоне то второе условие не проверять. Скорее всего так и будет, так как левая часть && даст
		// ноль, поэтому смысла в правой части не будет
		// Проверка валица на "localhost" в клиенте. Либо убрать, либо обработать иначе
		// С localhost клиент не цепляеца к серверу скорее всего из-за inet_addr()
		if((buffer[i] < 48 || buffer[i] > 58) && (buffer[i] != '.' && buffer[i] != '\0')){
			cout << "Error. Incorrect IP address\n";
			ip[0] = '\0';
			return;
		}
		ip[i] = buffer[i];
	}
	cout << ip << '\n';
}
*/


void mppp::setport(string buffer){
	//cin >> buffer;
	port = check_port(buffer);
}

