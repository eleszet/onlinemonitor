from tableHandling import addProtocol
import subprocess
import platform
from threading import Thread
import threading
import time

class handlePing(object):
    # constructor of the ping handle
    def __init__(self, *args):
        self.args = args
        self.protocolTable = args[0]
        self.hostName = args[1]
        self.interval = 1
        thread = threading.Thread(target=self.execPing, args=())
        #thread.daemon = True  # Daemonize thread
        thread.start()        # Start the execution

    # class for the ping
    def execPing(self):
        # Returns True if host responds to a ping request
        import subprocess, platform
        # Ping parameters as function of OS
        ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"
        args = "ping " + " " + ping_str + " " + self.hostName
        #msTime, issue 
        while True:
            try:
                result = extractPingResult(str(subprocess.check_output(args, shell=True)))
            except:
                result = 0,1        
            addProtocol(self.protocolTable, self.hostName, float(result[0]), str(result[1]))
            time.sleep(self.interval)
        return 
    
# internal functions
def extractPingResult(cmdReturn):
    import re
    # read CMD output 
    # split string separated by "ms"
    myList = cmdReturn.split(" ")
    numOut=0
    for entry in myList:
        # check if any string contains the value $$ms
        # windows output
        if  platform.system().lower()=="windows":
            if  re.search("ms", entry):
                testVar = entry
                num = re.findall(r"\d+", testVar)
                numOut = num[0]
                break
        # linux output
        else:
            if  re.search("time=", entry):
                testVar = entry
                numbers = [float(s) for s in re.findall(r'-?\d+\.?\d*', testVar)]
                numOut = float(numbers[0])
                break
    if numOut ==0:
        issue="1"
    else:
        issue="0"
    return numOut, issue
