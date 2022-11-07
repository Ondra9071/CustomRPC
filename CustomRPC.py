#    //   Fork project here: github.com/Ondra9071/CustomRPC

# ================================== INFO ================================== #

#    //                         © CustomRPC 2022
#    //   Version: 1.0.0
#    //   By Ondra907

#    //   Discord: Ondra907#9779
#    //   GitHub: github.com/Ondra9071

#    //   Thank you for using CustomRPC!

# ================================== IMPORTS ================================== #

from pypresence import Presence
import time
from colorama import Fore
import os

import ctypes
from re import I, X
ctypes.windll.kernel32.SetConsoleTitleW("Custom RPC | github.com/Ondra9071/CustomRPC")

os.system("cls")

class color:
    light = "\033[1m"
    
# ================================== TITLE ================================== #
def main():
    print(color.light, Fore.CYAN     + """
------------------------------------------------------------------------------------------- 

 ▄████▄   █    ██   ██████ ▄▄▄█████▓ ▒█████   ███▄ ▄███▓          ██▀███   ██▓███   ▄████▄  
▒██▀ ▀█   ██  ▓██▒▒██    ▒ ▓  ██▒ ▓▒▒██▒  ██▒▓██▒▀█▀ ██▒         ▓██ ▒ ██▒▓██░  ██▒▒██▀ ▀█  
▒▓█    ▄ ▓██  ▒██░░ ▓██▄   ▒ ▓██░ ▒░▒██░  ██▒▓██    ▓██░         ▓██ ░▄█ ▒▓██░ ██▓▒▒▓█    ▄ 
▒▓▓▄ ▄██▒▓▓█  ░██░  ▒   ██▒░ ▓██▓ ░ ▒██   ██░▒██    ▒██          ▒██▀▀█▄  ▒██▄█▓▒ ▒▒▓▓▄ ▄██▒
▒ ▓███▀ ░▒▒█████▓ ▒██████▒▒  ▒██▒ ░ ░ ████▓▒░▒██▒   ░██▒         ░██▓ ▒██▒▒██▒ ░  ░▒ ▓███▀ ░
░ ░▒ ▒  ░░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░   ░  ░         ░ ▒▓ ░▒▓░▒▓▒░ ░  ░░ ░▒ ▒  ░
  ░  ▒   ░░▒░ ░ ░ ░ ░▒  ░ ░    ░      ░ ▒ ▒░ ░  ░      ░           ░▒ ░ ▒░░▒ ░       ░  ▒   
░         ░░░ ░ ░ ░  ░  ░    ░      ░ ░ ░ ▒  ░      ░              ░░   ░ ░░       ░        
░ ░         ░           ░               ░ ░         ░               ░              ░ ░      
░                                                                                  ░        
                                                                                                                           
https://github.com/Ondra9071/CustomRPC
-------------------------------------------------------------------------------------------      
""")

# ================================== TITLE #2 ================================== #
def done():
    os.system("cls")
    print(color.light, Fore.GREEN     + """
------------------------------------------------------------------------------------------- 

 ▄████▄   █    ██   ██████ ▄▄▄█████▓ ▒█████   ███▄ ▄███▓          ██▀███   ██▓███   ▄████▄  
▒██▀ ▀█   ██  ▓██▒▒██    ▒ ▓  ██▒ ▓▒▒██▒  ██▒▓██▒▀█▀ ██▒         ▓██ ▒ ██▒▓██░  ██▒▒██▀ ▀█  
▒▓█    ▄ ▓██  ▒██░░ ▓██▄   ▒ ▓██░ ▒░▒██░  ██▒▓██    ▓██░         ▓██ ░▄█ ▒▓██░ ██▓▒▒▓█    ▄ 
▒▓▓▄ ▄██▒▓▓█  ░██░  ▒   ██▒░ ▓██▓ ░ ▒██   ██░▒██    ▒██          ▒██▀▀█▄  ▒██▄█▓▒ ▒▒▓▓▄ ▄██▒
▒ ▓███▀ ░▒▒█████▓ ▒██████▒▒  ▒██▒ ░ ░ ████▓▒░▒██▒   ░██▒         ░██▓ ▒██▒▒██▒ ░  ░▒ ▓███▀ ░
░ ░▒ ▒  ░░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░   ░  ░         ░ ▒▓ ░▒▓░▒▓▒░ ░  ░░ ░▒ ▒  ░
  ░  ▒   ░░▒░ ░ ░ ░ ░▒  ░ ░    ░      ░ ▒ ▒░ ░  ░      ░           ░▒ ░ ▒░░▒ ░       ░  ▒   
░         ░░░ ░ ░ ░  ░  ░    ░      ░ ░ ░ ▒  ░      ░              ░░   ░ ░░       ░        
░ ░         ░           ░               ░ ░         ░               ░              ░ ░      
░                                                                                  ░        

https://github.com/Ondra9071/CustomRPC
-------------------------------------------------------------------------------------------

RPC is running. To end RPC, press ENTER or close the program.
Thank you for using CustomRPC!

>>>> NOTE: The program must be open otherwise the RPC will disappear! <<<<


© CustomRPC 2022 | By Ondra907
""")

def error():
    os.system("cls")
    print(color.light, Fore.RED     + """
------------------------------------------------------------------------------------------- 

 ▄████▄   █    ██   ██████ ▄▄▄█████▓ ▒█████   ███▄ ▄███▓          ██▀███   ██▓███   ▄████▄  
▒██▀ ▀█   ██  ▓██▒▒██    ▒ ▓  ██▒ ▓▒▒██▒  ██▒▓██▒▀█▀ ██▒         ▓██ ▒ ██▒▓██░  ██▒▒██▀ ▀█  
▒▓█    ▄ ▓██  ▒██░░ ▓██▄   ▒ ▓██░ ▒░▒██░  ██▒▓██    ▓██░         ▓██ ░▄█ ▒▓██░ ██▓▒▒▓█    ▄ 
▒▓▓▄ ▄██▒▓▓█  ░██░  ▒   ██▒░ ▓██▓ ░ ▒██   ██░▒██    ▒██          ▒██▀▀█▄  ▒██▄█▓▒ ▒▒▓▓▄ ▄██▒
▒ ▓███▀ ░▒▒█████▓ ▒██████▒▒  ▒██▒ ░ ░ ████▓▒░▒██▒   ░██▒         ░██▓ ▒██▒▒██▒ ░  ░▒ ▓███▀ ░
░ ░▒ ▒  ░░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░   ░  ░         ░ ▒▓ ░▒▓░▒▓▒░ ░  ░░ ░▒ ▒  ░
  ░  ▒   ░░▒░ ░ ░ ░ ░▒  ░ ░    ░      ░ ▒ ▒░ ░  ░      ░           ░▒ ░ ▒░░▒ ░       ░  ▒   
░         ░░░ ░ ░ ░  ░  ░    ░      ░ ░ ░ ▒  ░      ░              ░░   ░ ░░       ░        
░ ░         ░           ░               ░ ░         ░               ░              ░ ░      
░                                                                                  ░        

https://github.com/Ondra9071/CustomRPC
-------------------------------------------------------------------------------------------

An error has occurred, restart the program.
""")

main()

# ================================== PICK ================================== #

rpcType = input("""What type of RPC do you want?
                
1 = Image, State
2 = Image, State & Button

: """)

os.system("cls")

# ================================== #1 RPC ================================== #

if (rpcType == "1"):
  main()
  inID = input("Discord App ID: ")
  inState = input("State: ")
  inLargeImg = input("Large Image: ")
  inLargeImgText = input("Large Image Text: ")

  client_id = inID
  RPC = Presence(client_id)
  RPC.connect()
  start_time = time.time()
  RPC.update(state=inState, large_image=inLargeImg, large_text=inLargeImgText, start=start_time)
  
# ================================== #2 RPC ================================== #
elif (rpcType == "2"):
  main()
  inID = input("Discord App ID: ")
  inState = input("State: ")
  inLargeImg = input("Large Image: ")
  inLargeImgText = input("Large Image Text: ")
  ButtonText = input("Button Text: ")
  ButtonURL = input("Button URL: ")
  
  client_id = inID
  RPC = Presence(client_id)
  RPC.connect()
  start_time = time.time()
  RPC.update(state=inState, large_image=inLargeImg, large_text=inLargeImgText, start=start_time, buttons = [{"label": ButtonText, "url": ButtonURL}])

else:
  error()
  input("Press ENTER to close the program.")
  
# ================================== THE END ================================== #

done()
end = input()

# ================================== © Custom RPC 2022 ================================== #