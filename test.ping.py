from tableHandling import addProtocol
import subprocess
import platform
import threading
import time
from pingHandler import extractPingResult
import shlex

ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"
args = "ping " + " " + ping_str + " " + "google.de"

output = subprocess.check_output("ping -c 1 heise.de", shell=True)
test = extractPingResult(str(subprocess.check_output(args)))
