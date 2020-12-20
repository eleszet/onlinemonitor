import os
import subprocess
import platform
from tableHandling import addHost 
from tableHandling import countTotalForHost10 
from tableHandling import countTotalForAll10
from tableHandling import retHosts
from tableHandling import retHostInfo10
from tableHandling import addProtocol
from tableHandling import countIssueHost10
from tableHandling import retAll10

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
    sumTotalPings = retNumVal(countTotalForAll10(pingProtocolTable))
    print(f"Results of the last pings (15 minutes past - total pings {sumTotalPings})")
    print("Host \t\t| total Pings \t\t\t| average reaction time")
    print("------------------------------------------------------------------------")
    # get results from protocol table for all hosts
    for entry in retAll10(pingProtocolTable):
              #hostname            sum pings               success               fails                         average ms
        print(entry[0] + " \t| " + str(entry[2]) + " - " + str(entry[4]) +  "/" + str(entry[3]) + " \t\t\t| " + str(entry[1]))

def clear():
    print("\033[H\033[J")

def hostInfo(pingProtocolTable, hostName):
    # get summary of the last 10 minutes
    return retHostInfo10(pingProtocolTable, hostName)

def retNumVal(numList):
    for sub in numList:
        return sub[0]
