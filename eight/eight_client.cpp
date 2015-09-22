#include <iostream>
#include "mppp.cpp"

/*
#include <>
#include <>
#include <>
*/

// https://stackoverflow.com/questions/8126512/deprecated-conversion-from-string-constant-to-char про строки и чары



int main(int argc, char *argv[]){
	if(argc < 2){
		cout << "ERROR: First argument must be IP address\n";
		return 0;
	}
	
	
	mppp client(43690, 1, argv[1]);
	
	
	return 0;
}
