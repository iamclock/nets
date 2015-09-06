sudo ip link set gre1 down
sudo ip link set gre2 down
sudo ip link set gre3 down

sudo ip tunnel del gre1
sudo ip tunnel del gre2
sudo ip tunnel del gre3
