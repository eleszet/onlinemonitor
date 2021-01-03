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
    console.clear()
    while newHost == "":
        showCurrentActiveHosts()
        hostName = input(
            "Enter Hostname or IP (Confirm empty line to start pinging): ")
        # >"" add new host to list
        if hostName > "" and hostName[0] != "-":
            tableHandling.addHost(hostName)
            # -r remove hpst from list
        elif(hostName[:2] == "-r"):
            splitVar = hostName.split()
            if(splitVar[1] > ""):
                tableHandling.rmHost(splitVar[1])
            # -t show last timeouts
        elif(hostName[:2] == "-t"):
            showTimeoutsInterval()
            # - return function to main (verbose/output only)
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
    showFails = False
    for result in pingResult:
        table.add_row(
            str(result[0]),                             # hostname

            str(result[2]),  # sum of pings sent to this host in last x minutes

            # formatted avg reaction time
            str("{:.2f}".format(result[1]).zfill(5)),
            str(result[4]),                             # failed pings
            str(result[3])                              # successed pings
        )
        sumPings += result[2]
        if result[3] > 0:
            showFails = True
    totalPings = tableHandling.countAllProtocol()
    # caption with total pigns / pings during last interval
    for result in totalPings:
        table.caption = "Total " + \
            str(result[0]) + " | Interval " + str(sumPings)
    console.clear()
    console.print(table)
    # failed pings? show table of failed pings
    if(showFails):
        showTimeoutsInterval()
    # 5sec delay
    time.sleep(5)


def showCurrentActiveHosts():
    # create objects for console and table
    table = Table(show_header=True, header_style="bold magenta")
    hostList = tableHandling.retHosts()
    table.add_column("Host")
    for result in hostList:
        table.add_row(
            str(result[0])  # hostname
        )
    console.clear()
    console.print(table)


def showTimeoutsInterval():
    # create objects for console and table
    table = Table(show_header=True, header_style="bold magenta")
    table.title = "Last timeouts"
    table.add_column("Hosts")
    table.add_column("Time of timeout")
    # fetch results of the pings and write into table
    timeoutlist = tableHandling.getTimeoutsIntervall()
    for result in timeoutlist:
        table.add_row(
            str(result[0]),
            str(result[1]),
        )
    console.print(table)
    input()
