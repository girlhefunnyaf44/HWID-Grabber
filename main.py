import pyperclip
import subprocess
import colorama
from colorama import init
init()
import time

s1 = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
pyperclip.copy(s1)
s2 = pyperclip.paste()


print(colorama.Fore.BLACK + " ----------------------------")
print(colorama.Fore.BLACK + " ----------------------------")

print(colorama.Fore.GREEN + "  _____     ____")
print(colorama.Fore.GREEN + " /      \  |  o | ")
print(colorama.Fore.GREEN + "|        |/ ___\| ")
print(colorama.Fore.GREEN + "|_________/     ")
print(colorama.Fore.GREEN + "|_|_| |_|_|")


print(colorama.Fore.BLACK + " ----------------------------")
print(colorama.Fore.RED + "HWID Copied to Clipboard!")
print(colorama.Fore.BLACK + " ----------------------------")

print(s2)
time.sleep(5.5)    # Pause 10.5 seconds
