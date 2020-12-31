from tableHandling import addHost 
from tableHandling import retAll10
import tableHandling
import time

def enterNewHost():
    newHost=""
    while newHost == "":
        hostName = input("Hostname or IP (Confirm empty line to start pinging): ") 
        if hostName>"":
            addHost(tableHandling.hostTable, hostName)
        else:
            break

def showHostList():
    while True:
        clear()
        # read pings of the last 10 minutes
        pingResult = retAll10(tableHandling.protocolTable)
        sumPings = 0
        for entry in pingResult:
            sumPings = sumPings + entry[2]
        print(f"Results of the last pings (15 minutes past - total pings {sumPings})")
        print("Host \t\t| total Pings \t\t\t| average reaction time")
        print("------------------------------------------------------------------------")
        # get results from protocol table for all hosts
        for entry in pingResult:
                #hostname            sum pings               success               fails                         average ms
            print(entry[0] + " \t| " + str(entry[2]) + " - " + str(entry[4]) +  "/" + str(entry[3]) + " \t\t\t| " + str(entry[1]))
        time.sleep(1)

def clear():
    print("\033[H\033[J")
