#! /usr/bin/python3







import sys,tty,termios
class _Getch:
	def __call__(self):
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(sys.stdin.fileno())
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch

def get():
	inkey = _Getch()
	while(1):
		k=inkey()
		if k!='':break
	print('you pressed', ord(k))


char = _Getch()
while True:
	char_new = char()
	if char_new != '':break
print(ord(char_new))
if char_new == '^[[A':
	print("UP")




'''
string = input("enter: ")
parsed_string = string.split(" ")

print(parsed_string[0])
'''



