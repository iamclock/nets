#include <iostream>
#include <cstring>

using namespace std;



unsigned short int check_port(char *buffer){
	// добавить обработку шестнадцатеричных и восьмеричных чисел
	int number = 0;
	int len_buffer = strlen(buffer);
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


int main(){
	
	char buffer[42];
	unsigned short int p;
	cin >> buffer;
	p = check_port(buffer);
	cout << p << '\n';
	return 0;
}