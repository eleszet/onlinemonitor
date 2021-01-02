import tableHandling
import time
import rich
from rich import print
from rich.console import Console
from rich.table import Table

console = Console()


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
    with console.status("[green]Refreshing...") as status:
        while True:
            showPings()


def showPings():
    # create objects for console and table
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Host")
    table.add_column("pings")
    table.add_column("avg ms")
    table.add_column("success", style="green")
    table.add_column("fails", style="red")
    # fetch results of the pings and write into table
    pingResult = tableHandling.retAll10()
    sumPings = 0
    for result in pingResult:
        table.add_row(
            str(result[0]),                             # hostname
            # sum of pings sent to this host in last x minutes
            str(result[2]),
            # formatted avg reaction time
            str("{:.2f}".format(result[1]).zfill(5)),
            str(result[4]),                             # failed pings
            str(result[3])                              # successed pings
        )
        sumPings += result[2]
    totalPings = tableHandling.countAllProtocol()
    # print table in console
    for result in totalPings:
        table.caption = "Total " + \
            str(result[0]) + " | Interval " + str(sumPings)
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
