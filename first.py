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


def dict_conc(obj_dict):
	conc = ''
	for element in obj_dict:
		conc += element
	return conc



def interface(interface, number):
	#check = subprocess.Popen("ifconfig -a".split(" "), stdout=subprocess.PIPE)
	#check = subprocess.Popen(["awk", "{print $1}"], stdout=subprocess.PIPE, stdin=check.stdout)
	#check = subprocess.Popen("grep eth".split(" "), stdout=subprocess.PIPE, stdin=check.stdout)
	#string = check.stdout.read(),decode("utf-8")
	#print(string)
	
	
	
	# Здесь может быть глюк
	check = subprocess.Popen(("ifconfig "+interface+str(number)).split(" "), stdout=subprocess.PIPE)
	
	check = check.stdout.read().decode("utf-8")
	
	if len(check) == 0:
		return
	
	if interface == "loopback":
		inter = "lo"
	else:
		inter = "eth"
	
	while True:
		string = input("router#"+interface+"> ")
		if string == '' or string == "quit" or string == "done":
			if string == "quit" or string == "done":
				break
			pass
		if string == "shutdown":
			subprocess.call("sudo ifconfig "+inter+str(number)+" down", shell=True)
		if string == "no shutdown":
			subprocess.call("sudo ifconfig "+inter+str(number)+" up", shell=True)
		parsed_string = string.split(" ")
		length_parstr = len(parsed_string)
		index = 0
		if parsed_string[index] == "no":
			index += 1
			if length_parstr == 1:
				fail = 1
				print("Command \"no\" must use with arguments. Type help for more information.")
		if parsed_string[index] == "ip" and fail == 0:
			index += 1
			if length_parstr > 1 and parsed_string[index] == "address":
				index += 1
				if length_parstr > 2 and parsed_string[index] == "add" or "del":
					ip_adr = parsed_string[index].split('.')
					index += 1
					if len(ip_adr) == 4:
						ip_adr = dict_conc(ip_adr)
						try:
							ip_adr = int(ip_adr)
						except ValueError:
							print("Incorrect IP address")
						else:
							if length_parstr > 3:
								mask = parsed_string[index].split('.')
								index += 1
								if len(mask) == 4:
									#mask = dict_conc(mask)
									for i in len(mask):
										try:
											check_mask = int(mask[i])
										except ValueError:
											fail = 1
											print("Incorrect mask")
									if fail == 0:
										subprocess.call("ifconfig "+intere+str(number)+" "+parsed_string[index-2]+" netmask "+parsed_string[index-1]+" up", shell=True)
								else:
									print("Incorrect mask")
					else:
						print("Incorrect IP address")
						
							
		elif parsed_string[index] == "no":
			#WORK_IN_PROGRESS
			print("Work in progress")
		#else:
			
	return





"""
show interface {ethernet | loopback} number
ip route prefix mask ip-address
no ip route prefix mask ip-address
interface {ethernet | loopback} number
"""


req_help = "help"
history = "history"
ip_routing = "ip routing"
no_ip_routing = "no ip routing"


#len_history = 256
#history = []
#i = 0
string = None
ipRoutingMode = False


while True:#string != "exit" and string != "off" and string != "quit":
	#if i == len_history:
		#i = 0;
	fail = 0
	string = input("router> ")
	#key = ord(getch())
	#if key == 
	#history[i] = string

		
		#subprocess.Popen("ip route")
	if string == '' or string == 'off' or string == "quit" or string == "exit":
		if string == 'off' or string == "quit" or string == "exit":
			break
		pass
	elif string == ip_routing: # ip routing - включение режима маршрутизации
		if ipRoutingMode == True:
			print("ip routing mode is already on", sep="")
		else:
			print("ip routing mode is on", sep="")
			ipRoutingMode = True
	elif string == no_ip_routing: # no ip routing - отключение режима маршрутизации
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
		if parsed_string[index] == "show": # show ip route; show interfaces; show interface {ethernet | loopback} number
			if length_parstr == 1:
				fail = 1
				print("Command \"show\" must use with arguments. Type help for more information.")
			else:
				index += 1
		if parsed_string[index] == "interfaces" or parsed_string[index] == "interface": #interface {ethernet | loopback} number
			if index == 0 and parsed_string[index] == "interfaces":
				pass
			else:
				index += 1
				if parsed_string[index-1] == "interface":
					if parsed_string[index] == "ethernet" or parsed_string[index] == "loopback":
						index += 1
						few = 1
						if index <= length_parstr:
							if index == 3:
								if length_parstr > 3:
									few = 0
									try:
										int(parsed_string[index])
									except ValueError:
										print("Incorrect argument. Must be a number")
									else:
										inter = "lo"
										if parsed_string[index-1] == "ethernet":
											inter = "eth"
										subprocess.call("ifconfig "+inter+parsed_string[index], shell=True)
										index += 1
							else:
								if index < length_parstr:
									few = 0
									try:
										numb = int(parsed_string[index])
									except ValueError:
										print("Third argument expected to be a number")
									else:
										index += 1
										if parsed_string[index-2] == "ethernet":
											interface("eth", int(parsed_string[index-1]))
										if parsed_string[index-2] == "loopback":
											interface("lo", int(parsed_string[index-1]))
						if few == 1:
							print("Too few arguments for this command")
					else:
						print("Command ", parsed_string[index-1], " not found", sep="")
				elif parsed_string[index-1] == "interfaces":
					if index == length_parstr:
						subprocess.call("ifconfig -a", shell=True)
					else:
						print("Unknown command \""+parsed_string[index]+"\" for \"interfaces\"")
						index += 1
				else:
					print("Command \"interface\" must use with arguments. Type help for more information")
		elif parsed_string[index] == "no" and index == 0:
			index += 1
		elif parsed_string[index] == "ip":
			index += 1
			if length_parstr > 2:
				index += 1
				if parsed_string[index-1] == "route":
					if parsed_string[0] == "show":
						subprocess.call("netstat -rn", shell=True)
					else:
						if parsed_string[0] == "no":
							#WORK_IN_PROGRESS
							print("work in progress. Expected to be \"no ip route prefix mask ip-address - добавление статического маршрута\" condition")
						else:
							#WORK_IN_PROGRESS
							print("work in progress. Expected to be \"ip route prefix mask ip-address - добавление статического маршрута\" condition")
				else:
					print("Command ", parsed_string[index-1], " not found", sep="")
			else:
				print("Too few arguments for \"show\" command. Type help for more information.")
		
				
		'''
		elif parsed_string[index] == "interface": #interface {ethernet | loopback} number
			index += 1
			if length_parstr > 1:
				index += 1
				if parsed_string[index-1] == "ethernet" or parsed_string[index-1] == "loopback":
					if length_parstr > 2:
						try:
							numb = int(parsed_string[index])
						except ValueError:
							print("Third argument expected to be a number")
						else:
							index += 1
							if parsed_string[index-2] == "ethernet":
								interface("eth", int(parsed_string[index-1]))
							if parsed_string[index-2] == "loopback":
								interface("lo", int(parsed_string[index-1]))
					else:
						print("Too few arguments for this command")
				else:
					print("Command ", parsed_string[index-1], " not found", sep="")
			else:
				print("Command \"interface\" must use with arguments. Type help for more information")
		'''
		if index < length_parstr:
			print("Command ", parsed_string[index], " not found", sep="")
		#for item in parsed_string:
		#	parsed_string.remove(item)
		
		
		
		
		
		
	'''
	elif string == history:
		for j in history:
			print(history[j],"\n", sep="")
	
	else:
		flag = False
	++i
	sleep(0.01)
	
	if len(parsed_string) > 3:
		print(parsed_string[3])
	'''
	















