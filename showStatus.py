import os
import subprocess, platform
from tableHandling import addHost 
from tableHandling import countTotalForHost10 
from tableHandling import countTotalForAll10
from tableHandling import retHosts
from tableHandling import retHostInfo10
from tableHandling import addProtocol
from tableHandling import countIssueHost10

def enterNewHost(hostTable):
    newHost=""
    while newHost == "":
        hostName = input("Hostname or IP (Confirm empty line to start pinging): ") 
        if hostName>"":
            addHost(hostTable, hostName)
        else:
            break

def showHostList(hostTable, pingProtocolTable, hostList):
    clear()
    print("Results of the last pings (10 minutes past)")
    for entry in hostList:
        hostInfoList = hostInfo(pingProtocolTable, entry[0])
        # sum of pings for host
        sumPing = retNumVal(countTotalForHost10(pingProtocolTable, entry[0]))
        # sum of fails for host
        sumFail = retNumVal(countIssueHost10(pingProtocolTable, entry[0], "1"))
        # sum of succesful pings for host
        sumSuccess = retNumVal(countIssueHost10(pingProtocolTable, entry[0], "0"))
        for sub in hostInfoList:
            print("Host " + sub[0] + " Total pings: " + str(sumPing) + " - " + str(sumSuccess)+  "/" + str(sumFail) + " Avg time (ms) " + str(sub[1]))

def clear():
    print("\033[H\033[J")

def hostInfo(pingProtocolTable, hostName):
    # get summary of the last 10 minutes
    return retHostInfo10(pingProtocolTable, hostName)

def retNumVal(numList):
    for sub in numList:
        return sub[0]