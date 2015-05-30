#! /usr/bin/python3



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


show_ip_route = "show ip route"
show_interfaces = "show interfaces"
show interface {ethernet | loopback} number
ip route prefix mask ip-address
no ip route prefix mask ip-address
interface {ethernet | loopback} number



string = input("router> ")
print(x)

if string == show_ip_route:
	