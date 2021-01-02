import tableHandling
import time


def enterNewHost():
    # enter new host
    # option
    # -r --> remove host
    # -v --> ping without console output
    # -o --> only show result without start pinging
    newHost = ""
    while newHost == "":
        showCurrentActiveHosts()
        hostName = input(
            "Hostname or IP (Confirm empty line to start pinging): ")
        if hostName > "" and hostName[0] != "-":
            tableHandling.addHost(hostName)
        elif(hostName[:2] == "-r"):
            splitVar = hostName.split()
            if(splitVar[1] > ""):
                tableHandling.rmHost(splitVar[1])
        elif hostName > "" and hostName[0] == "-":
            return hostName
        else:
            return""


def Loop():
    while True:
        time.sleep(1)


def showPingsLoop():
    while True:
        showPings()


def showPings():
    clear()
    # read pings of the last 10 minutes
    pingResult = tableHandling.retAll10()
    sumPings = 0
    for entry in pingResult:
        sumPings = sumPings + entry[2]
    print(
        f"Results of the last pings (15 minutes past - total pings {sumPings})")
    print("Host \t\t| total Pings \t\t\t| average reaction time")
    print("------------------------------------------------------------------------")
    # get results from protocol table for all hosts
    for entry in pingResult:
        # hostname            sum pings               success               fails                         average ms
        print(entry[0] + " \t| " + str(entry[2]).zfill(3) + " - " + str(entry[4]).zfill(3) +
              "/" + str(entry[3]).zfill(3) + " \t\t\t| " + "{:.2f}".format(entry[1]).zfill(5) + " ms")
    time.sleep(1)


def showCurrentActiveHosts():
    # show list of currentactive hosts
    clear()
    hostList = tableHandling.retHosts()
    print("Current Hostnames: ")
    for host in hostList:
        print("- " + str(host[0]))


def clear():
    print("\033[H\033[J")
