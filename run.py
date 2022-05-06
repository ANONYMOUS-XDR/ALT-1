import os
import sys
import time 
import platform
os.system('git pull')
try:
	import requests
except:
	os.system('pip install requests')
	os.system('pip2 install requests')
import requests
termux_bit = platform.architecture()[0]
if termux_bit == '64bit':
    from ALT import main_menu
    main_menu()
elif termux_bit == '32bit':
	from ALT32 import main_menu
    main_menu()