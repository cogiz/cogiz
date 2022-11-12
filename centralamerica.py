import worldcaps
import canada
import usa
import caribbean
import southamerica
import asia
import mideast
import europe
import africa
import australia
import subprocess as sp
from time import sleep
import sys
import os
import contextlib
import re

def main():  

	CENTRALAMERICA = ["Belize", "Costa Rica", "El Salvador", "Guatemala", "Honduras", "Nicaragua", "Panama"]

	CENTRALAMERICACC = ["Belmopan", "San Jose", "San Salvador", "Guatemala City", "Tegucigalpa", "Managua", "Panama City"]

	tmp = sp.call('clear',shell=True)
	selection = print("\033[2;13HYou have chosen \u001b[1mCentral America.\033[0m")
	y = len(CENTRALAMERICA)
	score = 0

	for p in range(len(CENTRALAMERICA)):

		print("\033[2;13HYou have chosen \u001b[1mCentral America.\033[0m")       
		print("\033[4;13HThere are %d Countries in Central America." % y)
		print("\033[6;13HLet's see how well you know your Central American geography.")
		print("\033[8;13HGOOD LUCK!")
		print("\033[10;30H*** Central America ***")
		print("\033[12;10H*******************************************************************")
		guess = str(input("\033[14;10H\033[0mWhat is the Capital of {}?: \033[0m".format(CENTRALAMERICA[p], p + 1)))

		if titlecase(guess) in CENTRALAMERICACC[p]:
			print("\033[16;10H\033[1;32mCongratulations! \033[0mYou are correct.")
			score += 1
			sleep(2)
			tmp = sp.call('clear', shell=True)
		else:
			print("\033[16;10H\033[1;31mSorry! \033[0mYou guessed wrong. The answer was \033[1;33m{}\033[0m".format(CENTRALAMERICACC[p]))
			score += 0
			sleep(2)
			tmp = sp.call('clear', shell=True)

	total = len(CENTRALAMERICA)
	divisor = score
	result = score / total * 100
	#quotient(score, total)
	print("\033[2;13HYou have chosen \u001b[1mCentral America.\033[0m")
	print("\033[4;13HThere are %d Countries in Central America." % y)
	print("\033[6;13HLet's see how well you know your Central American geography.")
	print("\033[8;13HGOOD LUCK!")
	print("\033[10;30H*** Central America ***")
	print("\033[12;10H\033[1;33m*******************************************************************\033[0m")
	print("\033[14;16HYou got a {} out of {} correct for a total of {}%".format(score, total, (round(result))))
	sleep(2)
	if result == 100:
		with contextlib.redirect_stdout(None):
			with open('/home/cogiz/boxscore.txt', 'r') as f:
				data = f.readlines()
			print (data)
			print (data[0])
			data[5] = "Central America      {}%\n".format(round(result))
	
		with open('/home/cogiz/boxscore.txt', 'w') as f:
			f.writelines( data )
			f.close()
	else:
		with contextlib.redirect_stdout(None):
			with open('/home/cogiz/boxscore.txt', 'r') as f:
				data = f.readlines()
			print (data)
			print (data[0])
			data[5] = "Central America       {}%\n".format(round(result))
	
		with open('/home/cogiz/boxscore.txt', 'w') as f:
			f.writelines( data )
			f.close()

	menu_reset()

	tmp = sp.call('clear',shell=True)
	
def region_menu():
	tmp = sp.call('clear',shell=True)
	print("\033[2;32H*** REGIONS ***\n", "\033[4;31H1.  Canada\n", "\033[6;31H2.  U.S.A.\n", "\033[8;31H3.  Caribbean\n",
		  "\033[10;31H4.  Central America\n", "\033[12;31H5.  South America\n", "\033[14;31H6.  Asia\n", "\033[16;31H7.  Middle East\n",
		  "\033[18;31H8.  Europe\n", "\033[20;31H9.  Africa\n", "\033[22;30H10.  Australia\n")
	choice = input("\033[24;30HEnter Region #: ")
	print("\n\n")
	if choice == "1":
		tmp = sp.call('clear',shell=True)
		canada.main()
	if choice == "2":
		tmp = sp.call('clear',shell=True)
		usa.main()
	if choice == "3":
		tmp = sp.call('clear',shell=True)
		caribbean.main()
	if choice == "4":
		tmp = sp.call('clear',shell=True)
		main()
	if choice == "5":
		tmp = sp.call('clear',shell=True)
		southamerica.main()
	if choice == "6":
		tmp = sp.call('clear',shell=True)
		asia.main()
	if choice == "7":
		tmp = sp.call('clear',shell=True)
		mideast.main()
	if choice == "8":
		tmp = sp.call('clear',shell=True)
		europe.main()
	if choice == "9":
		tmp = sp.call('clear',shell=True)
		africa.main()
	if choice == "10":
		tmp = sp.call('clear',shell=True)
		australia.main()

def menu_reset():
	choice = input("\033[18;15HPress [b] for Box Score or [r] for Region Menu: ")
	print("\n\n")
	if choice == "b":
		tmp = sp.call('clear',shell=True)
		os.system("cat /home/cogiz/boxscore.txt")
		choice2 = input("\033[25;0HPress [r] for Region Menu or [q] to quit: ")
		print("\n\n")
		if choice2 == "r":
			region_menu()
		if choice2 == "q":
			tmp = sp.call('clear',shell=True)
			print("\033[13;24HThanks for playing....Good Bye!")
			sleep(2)
			tmp =sp.call('clear',shell=True)
			sys.exit()

	if choice == "r":
		region_menu() 

def titlecase(s):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                   lambda mo: mo.group(0)[0].upper() +
                             mo.group(0)[1:].lower(),
                   s)    



if __name__ == '__main__':
	main()