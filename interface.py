#! /usr/bin/python3



import subprocess



def dict_conc(obj_dict):
	conc = ''
	for element in obj_dict:
		conc += element
	return conc


def mask_wizard(mask):
	numer = 0
	for i in len(mask):
		if mask[i] == "128":
			numer += 1
		elif mask[i] == "192":
			numer += 2
		elif mask[i] == "224":
			numer += 3
		elif mask[i] == "240":
			numer += 4
		elif mask[i] == "248":
			numer += 5
		elif mask[i] == "252":
			numer += 6
		elif mask[i] == "254":
			numer += 7
		elif mask[i] == "255":
			numer += 8
		else:
			return -1




def interface(interface, number):
	#check = subprocess.Popen("ifconfig -a".split(" "), stdout=subprocess.PIPE)
	#check = subprocess.Popen(["awk", "{print $1}"], stdout=subprocess.PIPE, stdin=check.stdout)
	#check = subprocess.Popen("grep eth".split(" "), stdout=subprocess.PIPE, stdin=check.stdout)
	#string = check.stdout.read(),decode("utf-8")
	#print(string)
	
	if interface == "loopback":
		inter = "lo"
	else:
		inter = "eth"
	
	# Здесь может быть глюк
	check = subprocess.Popen(("ifconfig "+inter+str(number)).split(" "), stdout=subprocess.PIPE)
	
	check = check.stdout.read().decode("utf-8")
	
	if len(check) == 0:
		return
	
	
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
				#fail = 1
				print("Command \"no\" must use with arguments. Type help for more information.")
		if parsed_string[index] == "ip":
			index += 1
			if length_parstr > 1 and parsed_string[index] == "address":
				index += 1
				if length_parstr > 2:
					ip_adr = parsed_string[index].split('.')
					#index += 1
					if len(ip_adr) == 4:
						for i in len(ip_addr):
							try:
								check_ip_adr = int(ip_adr[i])
							except ValueError:
								fail = 1
								print("Incorrect IP address")
						if fail == 0:
							index += 1
							if length_parstr > 3:
								mask = parsed_string[index].split('.')
								#index += 1
								if len(mask) == 4:
									#mask = dict_conc(mask)
									for i in len(mask):
										try:
											check_mask = int(mask[i])
										except ValueError:
											fail = 1
											print("Incorrect mask")
									if fail == 0:
										numb_mask = mask_wizard(mask)
										if numb != -1:
											index += 1
											if index == 4:
												subprocess.call("ip addr add "+parsed_string[index-2]+"/"+str(numb_mask)+"dev "+inter+str(number), shell=True)
											else:
												subprocess.call("ip addr del "+parsed_string[index-2]+"/"+str(numb_mask)+"dev "+inter+str(number), shell=True)
										else:
											print("Incorrect mask")
								else:
									print("Incorrect mask")
					else:
						print("Incorrect IP address")
	return


while True:
	string = input("Choose interface(ethernet/loopback) and numba: ")
	if string == "off":
		break
	parsedString = string.split(" ")
	interface(parsedString[0], int(parsedString[1]))



