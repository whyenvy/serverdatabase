#sdata maker by whyenvy
#Leave a credit
#inspired by NumeX

import os, sys, time

print("||==================================||")
print("[+] Made by envy#0449")
print("[+] Github : https://github.com/whyenvy")
print("[+] Usage : python3 serverdata.py ")
print("||==================================||")

serverip = input("[>]Server IP : ")
sport = input("[>]Server Port : ")
mainmsg = input("[>] Maintenance Message : ")

print("\n")

sd = open("server_data.php", "w")
sd.write(
    f"server|{serverip}\nport|{sport}\ntype|1\n#maint|{mainmsg}\n\nbeta_server|127.0.0.1\nbeta_port|17091\n\nbeta_type|1\nmeta|localhost\nRTENDMARKERBS1001"
)
sd.close()
time.sleep(1)
print("[>]server_data.php has been created.")
input("Click enter to close.")