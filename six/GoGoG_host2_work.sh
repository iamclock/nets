#!/bin/bash

ip_local=$(ifconfig eth0 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}')
echo IP = $ip_local
echo Enter ip_remote
read ip_remote

sudo ip tunnel add gre1 mode gre remote $ip_remote local $ip_local
sudo ip link set gre1 up
sudo ip addr add 10.0.1.2/24 dev gre1
#sudo ip route add 10.0.1.0/24 dev gre1

sudo ip tunnel add gre2 mode gre remote 10.0.1.1 local 10.0.1.2
sudo ip link set gre2 up
sudo ip addr add 10.0.3.2/24 dev gre2
#sudo ip route add 10.0.3.0/24 dev gre2

sudo ip tunnel add gre3 mode gre remote 10.0.3.1 local 10.0.3.2
sudo ip link set gre3 up
sudo ip addr add 10.0.5.2/24 dev gre3
#sudo ip route add 10.0.5.0/24 dev gre3

echo -e "GRE-over-GRE-over-GRE \nFor testing input 'ping 10.0.5.1'"
