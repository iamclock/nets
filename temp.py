#! /usr/bin/python3

import subprocess



'''
check = subprocess.Popen("ifconfig -a".split(" "), stdout=subprocess.PIPE)
check = subprocess.Popen(["awk", "{print $1}"], stdout=subprocess.PIPE, stdin=check.stdout)
check = subprocess.Popen("grep lo".split(" "), stdout=subprocess.PIPE, stdin=check.stdout)

string = check.stdout.read().decode("utf-8")

print(len(string))
print(string)

'''

'''

while True:
	numb = input("type numb: ")
	try:
		numb = int(numb)
	except ValueError:
		print("invalid number")
	else:
		try:
			subprocess.call("ifconfig eth"+str(numb), shell=True)
		except 

'''

'''

numb = 1
check = subprocess.Popen(("ifconfig lo"+str(numb)).split(" "), stdout=subprocess.PIPE)

check = check.stdout.read().decode("utf-8")

print(len(check))

#check = check.split(" ")

print(check)

'''

def dict_conc(obj_dict):
	conc = ''
	for element in obj_dict:
		conc += element
	return conc

string = "192.168.25"

ip_adr = string.split('.')
print(len(ip_adr))
ip_adr = dict_conc(ip_adr)
print(ip_adr)
try:
	ip_adr = int(ip_adr)
except ValueError:
	print("Invalid IP address")
else:
	print("OK")














