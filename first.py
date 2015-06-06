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

show_ip_route = "sir"#"show ip route"
show_interfaces = "si"#"show interfaces"
req_help = "help"
history = "h"
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
flag = True
ipRoutingMode = False



while string != "shutdown" and string != "exit" and string != "off":
	#if i == len_history:
		#i = 0;
	if flag == False:
		print("command ", string, " not found", sep="")
		flag = True
	
	string = input("router> ")
	#key = ord(getch())
	#if key == 
	#history[i] = string

	if string == show_ip_route:
		subprocess.call("netstat -rn", shell=True)
		#subprocess.Popen("ip route")
	elif string == show_interfaces:
		subprocess.call("ifconfig", shell=True)
		#subprocess.Popen("ifconfig")
	elif string == ip_routing:
		if ipRoutingMode == True:
			print("ip routing mode is already on\n", sep="")
		else:
			print("ip routing mode is on\n", sep="")
			ipRoutingMode = True
	elif string == no_ip_routing:
		if ipRoutingMode == False:
			print("ip routing mode is already off\n", sep="")
		else:
			print("ip routing mode is off\n", sep="")
			ipRoutingMode = False
	elif string == req_help:
		print(str_help)
	#elif string == history:
		#for j in history:
			#print(history[j],"\n", sep="")
	elif string == '':
		pass
	else:
		flag = False
	#++i
	#sleep(0.01)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	