#! /usr/bin/python3



import subprocess
#from time import sleep
#from msvcrt import getch()


"""
Написать сценарий, эмулирующий командную строку Cisco IOS в рамках 
конфигурирования основных сетевых параметров операционной системы. Реализовать 
следующие команды:
		show interface {ethernet | loopback} number - вывод информации о заданном интерфейсе
		ip route prefix mask ip-address - добавление статического маршрута к сети prefix с маской mask через шлюз ip-address
		no ip route prefix mask ip-address - удаление статического маршрута
		interface {ethernet | loopback} number - выбор интерфейса для конфигурирования
				ip address ip-address mask - задание IP-адреса и сетевой маски для выбранного интерфейса
				no ip address ip-address mask - удаление IP-адреса и сетевой маски для выбранного интерфейса
				shutdown - отключение интерфейса
				no shutdown - включение интерфейса
		ip name-server server-address1 [server-address2] - задание DNS-сервера
		no ip name-server server-address1 [server-address2] - удаление DNS-сервера
"""
str_help = "	show ip route - вывод таблицы маршрутизации\n	show interfaces - вывод информации обо всех сетевых интерфейсах\n	show interface {ethernet | loopback} number - вывод информации о заданном интерфейсе\n	ip route prefix mask ip-address - добавление статического маршрута к сети prefix с маской mask через шлюз ip-address\n	no ip route prefix mask ip-address - удаление статического маршрута\n	interface {ethernet | loopback} number - выбор интерфейса для конфигурирования\n		ip address ip-address mask - задание IP-адреса и сетевой маски для выбранного интерфейса\n		no ip address ip-address mask - удаление IP-адреса и сетевой маски для выбранного интерфейса\n		shutdown - отключение интерфейса\n		no shutdown - включение интерфейса\n	ip name-server server-address1 [server-address2] - задание DNS-сервера\n	no ip name-server server-address1 [server-address2] - удаление DNS-сервера\n	ip routing - включение режима маршрутизации\n	no ip routing - отключение режима маршрутизации\n"

req_help = "help"
history = "history"
ip_routing = "ip routing"
no_ip_routing = "no ip routing"


"""
show interface {ethernet | loopback} number
ip route prefix mask ip-address
no ip route prefix mask ip-address
interface {ethernet | loopback} number
"""

#len_history = 256
#history = []
#i = 0
string = None
ipRoutingMode = False


def ethernet(numb):
	
	
	
	#string = input("router#ethernet> ")
	print("router#ethernet> \n"+"router> ")
	
	
	




def loopback(numb):
	
	
	
	print("router#loopback> \n"+"router> ")
	#string = input("router#loopback> ")
	
	
	
	




while string != "exit" and string != "off" and string != "quit":
	#if i == len_history:
		#i = 0;
	
	string = input("router> ")
	#key = ord(getch())
	#if key == 
	#history[i] = string

		
		#subprocess.Popen("ip route")
	if string == '' or string == 'off' or string == "quit" or string == "exit":
		pass
	elif string == ip_routing:
		if ipRoutingMode == True:
			print("ip routing mode is already on", sep="")
		else:
			print("ip routing mode is on", sep="")
			ipRoutingMode = True
	elif string == no_ip_routing:
		if ipRoutingMode == False:
			print("ip routing mode is already off", sep="")
		else:
			print("ip routing mode is off", sep="")
			ipRoutingMode = False
	elif string == req_help:
		print(str_help)
	else:
		parsed_string = string.split(" ")
		length_parstr = len(parsed_string)
		index = 0
		if parsed_string[index] == "show":
			index += 1
			if length_parstr > 1:
				if parsed_string[index] == "interfaces" or parsed_string[index] == "interface":
					index += 1
					if length_parstr > 2:
						if parsed_string[index] == "ethernet":
							index += 1
							subprocess.call("ifconfig eth0", shell=True)
						elif parsed_string[index] == "loopback":
							index += 1
							subprocess.call("ifconfig lo", shell=True)
					else:
						subprocess.call("ifconfig -a", shell=True)
						#subprocess.Popen("ifconfig")
				elif parsed_string[index] == "ip":
					index += 1
					subprocess.call("netstat -rn", shell=True)
			else:
				print("command \"show\" must use with arguments. Type help for more information")
		elif parsed_string[index] == "interface":
			index += 1
			if length_parstr > 1:
				index += 1
				if parsed_string[index-1] == "ethernet":
					if length_parstr > 2:
						if parsed_string[index] < '9' and parsed_string[index] > '0':
							index += 1
							ethernet(int(parsed_string[index-1]))
						else:
							print("Third argument must be a number\n")
				elif parsed_string[index-1] == "loopback":
					loopback()
				else:
					print("command ", parsed_string[index-1], " not found", sep="")
			else:
				print("command \"interface\" must use with arguments. Type help for more information")
		if index < length_parstr:
			print("command ", parsed_string[index], " not found", sep="")
			
		for item in parsed_string:
			parsed_string.remove(item)
		
		
		
		
		
		
	
	#elif string == history:
		#for j in history:
			#print(history[j],"\n", sep="")
	
	#else:
		#flag = False
	#++i
	#sleep(0.01)
	
	#if len(parsed_string) > 3:
		#print(parsed_string[3])
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	