#!/usr/bin/python3

import os
import core
import getmac

r = core.r
p = core.pink
re = core.lred
y = core.yellow
g = core.lgreen
lc = core.lcyan
pu = core.purple
bo = core.bold
ul = core.ul

global macspoof
macspoof = "None Found"
mac_id = getmac.get_mac_address()

def start():
    try:
        core.clear()
        print("--------------------- \n")
        os.system("ifconfig")
        print("\n--------------------- \n")
        answer = input("Please type your wireless adapter's name (Default: wlan0): ")
        if answer == "":
            mon = "wlan0"
        else:
            mon = answer
        startup(mon)
    except KeyboardInterrupt:
        core.quit()
        
def startup(mon):
  core.clear()
  core.logo()
  print(r + ul + bo + "Welcome to Airline-Crack!" + r + "\n")
  print("Your device: " + core.checksystem())
  print("Your network interface: " + mon)
  print("Your original mac address: " + str(mac_id))
  os.system("macchanger -s " + mon)
  print("")
  print(r + "(" + lc + "1" + r + ")" + "  Scan MAC-Addresses/Devices on Network")
  print(r + "(" + lc + "2" + r + ")" + "  Become a specific MAC address")
  print(r + "(" + lc + "3" + r + ")" + "  Become a random MAC address")
  print(r + "(" + lc + "r" + r + ")" + "  Reload/Clear the screen")
  print(r + "(" + lc + "99" + r + ")" + " Exit the tool (CNTRL + C) \n")

  while True:
      answer = input(bo + "Airline" + r + "-" + re + "C" + y + "r" + g + "a" + lc + "c" + p + "k" + lc + " > " + r)
      if answer == "1":
          print("")
          os.system("sudo arp-scan -l")
          print("")
          save = input("Would you like to save these outputs? (Default = No): ")
          if save == "y" or save == "yes" or save == "Y" or save == "Yes" or save == "YES":
              savename = input("What would you like to call the file? (ex: moo): ")
              os.system("sudo arp-scan -l > " + savename + ".log")
              print("")
              input("Your output was saved in " + savename + ".log")
              startup(mon)
          else:
              input("\nAlright, your output was not saved.")
              startup(mon)
      elif answer == "2":
          print("")
          macspoof = input("Please type a specific Mac Address: ")
          print("")
          os.system("macchanger -m " + macspoof + " " + mon)
          print("")
          input("Finished! Please press {ENTER} to continue...")
          startup(mon)
      elif answer == "3":
          print("")
          macspoof = os.system("macchanger -r " + mon)
          print("")
      elif answer == "r":
          startup(mon)
      elif answer == "99":
          core.quit()
      elif answer == "exit":
          core.quit()
      else:
          print("\nThe choice '" + answer + "' was not found. Please pick a choice above. \n")
start()
