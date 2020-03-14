import os, sys
import time

location = input("Enter repo address: ")
os.system("git init")
time.sleep(5)
os.system("git add remote origin {}".format(location))
time.sleep(3)
os.system("git pull origin master")
exit()
