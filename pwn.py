import os

print("""
==================================
|     [Am I been pwned? ]        |
|    [well lets find out!]       |
|                                |
| [Created By: (Anikin Luke)]    |
|                                |
==================================
	""")

print("Enter a any password to check if its been pwned")

#while True:
#
#	ui = input("Enter here: ")
#
#	if(ui == '1'):
#		break
#	else:
#		os.system(f"cat /home/zimos/rockyou.txt| grep {ui}")

#DIR = open('/home/zimos/rockyou.txt', 'r')

def data1():

	LIST1 = open('wordlist/rockyou.txt', 'r')
	LIST = LIST1.read().splitlines() 
	return LIST

def data2():

	LIST1 = open('wordlist/darkc0de.txt', 'r')
	LIST = LIST1.read().splitlines() 
	return LIST


def main():

	global LIST, wlist

	ui = raw_input("Enter here: ")
	for i in LIST:
		if(i == ui):
			print '\nOH! BAD!!, your password is in the wordlist '+wlist
			break

		else:
			continue

	if(i != ui):
		print "NICE!! your password is not common and not in wordlist "+wlist


def darkc0de():

	LIST = data()
	ui = raw_input("Enter here: ")
	for i in LIST:
		if(i == ui):
			print '\nOH! BAD!!, your password is in the wordlist '+wlist 
			break

		else:
			continue

	if(i != ui):
		print "NICE!! your password is not common and not in wordlist "+wlist


while True:

	print("""

[1] ===== RockYou
[2] ===== darkc0de
[0] ===== exit
		""")


	ui = raw_input("select > ")
	if ui == "1":
		LIST = data1()
		wlist = "rockyou.txt"
		main()
		break

	elif ui == "2":
		LIST = data2()
		wlist = "darkc0de.txt"
		main()
		break

	elif ui == '0':
		break

	else:
		print("ERROR! pls select a number")
