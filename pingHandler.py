from tableHandling import addProtocol
import subprocess, platform



class handlePing(object):
    def __init__(self): 
        self.name = name
    # class for the ping
    def execPing(protocolTable, hostName):
        # Returns True if host responds to a ping request
        import subprocess, platform
        # Ping parameters as function of OS
        ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"
        args = "ping " + " " + ping_str + " " + hostName
        #extractPingResult = subprocess.call(args, shell=need_sh)
        msTime = extractPingResult(str(subprocess.check_output(args)))
        addProtocol(protocolTable, hostName, int(msTime[0]))
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
        if  re.search("ms", entry):
            testVar = entry
            numOut = re.findall("\d+", testVar)
            break
    return numOut