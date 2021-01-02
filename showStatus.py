import tableHandling
import time
import rich
from rich import print
from rich.console import Console
from rich.table import Table

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
    # create objects for console and table
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Host")
    table.add_column("Total Pings")
    table.add_column("Average MS")
    table.add_column("Success", style="green")
    table.add_column("Fails", style="red")
    # fetch results of the pings and write into table
    pingResult = tableHandling.retAll10()
    sumPings=0
    for result in pingResult:
        avgFormat = "{:.2f}".format(result[1]).zfill(5)
        table.add_row(
            str(result[0]), # hostname
            str(result[2]), # sum of pings sent to this host in last x minutes
            str(avgFormat), # formatted avg reaction time
            str(result[4]), # failed pings
            str(result[3])  # successed pings

        )
        sumPings+=result[2]
    # print table in console
    console.clear()
    console.print(table)
    # 5sec delay
    time.sleep(5)

def showCurrentActiveHosts():
    # show list of currentactive hosts  
    clear()
    hostList = tableHandling.retHosts()
    print("Current Hostnames: ")
    for host in hostList:
        print("- " + str(host[0]))


def clear():
    print("\033[H\033[J")
