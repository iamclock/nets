#include <iostream>
#include "mppp.cpp"
/*
#include <>
#include <>
#include <>
*/

// https://stackoverflow.com/questions/8126512/deprecated-conversion-from-string-constant-to-char про строки и чары



int main(){
	char myip[16] = "192.168.203.7";
	mppp client(myip, 43690, 1);
	
	
	
	return 0;
}
