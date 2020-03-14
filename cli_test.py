import os, sys
import time

#result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
#result.stdout

file_path = input("Enter file path here: ")
commit = input("Enter commit message: ")

os.system("cd\ ")
#now we are in the git repo address
os.system("cd {}".format(file_path))
#Pull incase of merge conflicts
#Push all files
os.system("git remote -v")

def git_args():
    os.system('git pull origin master')
    time.sleep(10)
    os.system('git add .')
    time.sleep(5)
    os.system("git commit -m '{}'".format(commit))
    time.sleep(2)
    os.system('git push origin master')
    time.sleep(30)
    exit()

git_args()
