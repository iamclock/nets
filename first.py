#! /usr/bin/python3



import subprocess
from time import sleep



"""
Написать сценарий, эмулирующий командную строку Cisco IOS в рамках 
конфигурирования основных сетевых параметров операционной системы. Реализовать 
следующие команды:

    show ip route - вывод таблицы маршрутизации
    show interfaces - вывод информации обо всех сетевых интерфейсах
    show interface {ethernet | loopback} number - вывод информации о заданном интерфейсе
    ip route prefix mask ip-address - добавление статического маршрута к сети 
prefix с маской mask через шлюз ip-address
    no ip route prefix mask ip-address - удаление статического маршрута
    interface {ethernet | loopback} number - выбор интерфейса для конфигурирования
        ip address ip-address mask - задание IP-адреса и сетевой маски для выбранного интерфейса
        no ip address ip-address mask - удаление IP-адреса и сетевой маски для выбранного интерфейса
        shutdown - отключение интерфейса
        no shutdown - включение интерфейса
    ip name-server server-address1 [server-address2] - задание DNS-сервера
    no ip name-server server-address1 [server-address2] - удаление DNS-сервера
    ip routing - включение режима маршрутизации
    no ip routing - отключение режима маршрутизации
"""


show_ip_route = "sir"#"show ip route"
show_interfaces = "si"#"show interfaces"
"""
show interface {ethernet | loopback} number
ip route prefix mask ip-address
no ip route prefix mask ip-address
interface {ethernet | loopback} number
"""

string = None
while string != "shutdown" and string != "exit" and string != "off":
	string = input("router> ")

	if string == show_ip_route:
		subprocess.call("netstat -rn", shell=True)
		#subprocess.Popen("ip route")
	elif string == show_interfaces:
		subprocess.call("ifconfig", shell=True)
		#subprocess.Popen("ifconfig")
	#elif string == :
		
	#sleep(0.01)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	