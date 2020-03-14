import sys
import subprocess

theproc = subprocess.Popen("cli_test.py", shell = True)
theproc.communicate()
