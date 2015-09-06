#include <iostream>
#include "mppp.cpp"
/*
#include <>
#include <>
#include <>
*/

// https://stackoverflow.com/questions/8126512/deprecated-conversion-from-string-constant-to-char про строки и чары


int main(){
	char myip[16] = "109.171.16.127";
	//std::cout << myip << '\n';
	mppp server(myip, 43690, 0);
	
	
	
	return 0;
}