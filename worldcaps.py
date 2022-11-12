import canada
import usa
import caribbean
import centralamerica
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
from pathlib import Path

def main():
	tmp = sp.call('clear', shell=True)
	print("\033[3;36HWORLDCAPS")
	print("\033[4;36H*********")
	print("\033[6;14HWorldcaps is a test of your knowledge of World Geography.")
	print("\033[8;14HChoose a Region of the World and then answer the question.")
	print("\033[10;14HFor each correct answer, one point is given.")
	print("\033[12;14H(Hint) Capital Letters and spelling are very important.")
	print("\033[14;36HGOOD LUCK!")
	print("\033[16;14H*********************************************************")
	sleep(3)
	print("\033[3;36HWORLDCAPS")
	print("\033[4;36H*********")
	print("\033[6;14HWorldcaps is a test of your knowledge of World Geography.")
	print("\033[8;14HChoose a Region of the World and then answer the question.")
	print("\033[10;14HFor each correct answer, one point is given.")
	print("\033[12;14H(Hint) Capital Letters and spelling are very important.")
	print("\033[14;36HGOOD LUCK!")
	print("\033[16;14H*********************************************************")
	#print("\033[18;30H1. Previous Box Score")
	#print("\033[20;30H2. Fresh Box Score")
	#selection = input("\033[22;30HEnter choice #: ")
	#print("\n\n")
	sleep(1)

	if Path("/home/cogiz/boxscore.txt").is_file():
		tmp = sp.call('clear',shell=True)
		print("\033[3;36HWORLDCAPS")
		print("\033[4;36H*********")
		print("\033[6;14HWorldcaps is a test of your knowledge of World Geography.")
		print("\033[8;14HChoose a Region of the World and then answer the question.")
		print("\033[10;14HFor each correct answer, one point is given.")
		print("\033[12;14H(Hint) Capital Letters and spelling are very important.")
		print("\033[14;36HGOOD LUCK!")
		print("\033[16;14H*********************************************************")
		print("\033[20;22HChecking for previous Box Scores ...")
		sleep(2)
		print("\033[20;22H                                          ")
		q = input("\033[20;18HBox Score already exists...keep it? (y/n): ")
		sleep(1)
		for a in q:
			if a == "y":
				pass
			if a == "n":
				print("\033[20;18H                                            ")
				print("\033[20;23HA fresh Box score has been created.")
				with open('/home/cogiz/boxscore.txt', 'w') as f:
					line1 = "    *** BOX SCORE ***\n"
					line2 = "\n"
					line3 = "Canada\n"       
					line4 = "Usa\n"
					line5 = "Caribbean\n"
					line6 = "Central America\n"
					line7 = "South America\n"                        
					line8 = "Asia\n"
					line9 = "Middle East\n"
					line10 = "Europe\n"
					line11 = "Africa\n"
					line12 = "Australia"
					f.writelines([line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12])
		sleep(1)
		pass
	else:
		tmp = sp.call('clear',shell=True)
		print("\033[3;36HWORLDCAPS")
		print("\033[4;36H*********")
		print("\033[6;14HWorldcaps is a test of your knowledge of World Geography.")
		print("\033[8;14HChoose a Region of the World and then answer the question.")
		print("\033[10;14HFor each correct answer, one point is given.")
		print("\033[12;14H(Hint) Capital Letters and spelling are very important.")
		print("\033[14;36HGOOD LUCK!")
		print("\033[16;14H*********************************************************")
		print("\033[20;22HA fresh Box score has been created.")
		with open('/home/cogiz/boxscore.txt', 'w') as f:
			line1 = "    *** BOX SCORE ***\n"
			line2 = "\n"
			line3 = "Canada\n"       
			line4 = "Usa\n"
			line5 = "Caribbean\n"
			line6 = "Central America\n"
			line7 = "South America\n"                         
			line8 = "Asia\n"
			line9 = "Middle East\n"
			line10 = "Europe\n"
			line11 = "Africa\n"
			line12 = "Australia"
			f.writelines([line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12])

	sleep(1)		
	tmp = sp.call('clear',shell=True)

	region_menu()

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
		centralamerica.main()
	if choice == "5":
		tmp = sp.call('clear',shell=True)
		southamerica.main()
	if choice == "6":
		tmp = sp.call('clear',shell=True)
		asia.main()
	if choice == "7":
		tmp =sp.call('clear',shell=True)
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

	
	
if __name__ == '__main__':
	main()


	