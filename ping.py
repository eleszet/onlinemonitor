# practicing some pythong 
# - using different files / functions
# - using local postgres DB wit hsome create/select/delete statements
# - show & maintain a host table
# - execute several ping commands parallel and store the result in a table

#import table functions
from tableHandling import checkTable
from tableHandling import createHostTable
from tableHandling import createProtocolTable
from tableHandling import retHosts
from pingHandler import handlePing
import time
from threading import Thread
from showStatus import showHostList
from showStatus import enterNewHost

# table names
hostTable = "hostnames"
pingProtocolTable = "pingprotocol"

# check & create tables
if(not checkTable(hostTable)):
    createHostTable(hostTable)
if(not checkTable(pingProtocolTable)):
    createProtocolTable(pingProtocolTable)

# check for new hostname and insert
enterNewHost(hostTable)

# fetch hosts
hostList = retHosts(hostTable)
# execute ping for available hosts
for entry in hostList:
    handle = handlePing(pingProtocolTable, entry[0])

#pingThread.join()
while True:
    # get host list
    hostList = retHosts(hostTable)
     # show results
    showHostList(hostTable, pingProtocolTable, hostList)
    time.sleep(2)
        