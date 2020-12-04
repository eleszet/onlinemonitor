#import table functions
from tableHandling import checkTable
from tableHandling import createHostTable
from tableHandling import createProtocolTable
from tableHandling import openConnection
from tableHandling import addHost
from tableHandling import retHosts

# table names
hostTable = "hostnames"
pingProtocolTable = "pingprotocol"

# check & create tables
if(not checkTable(hostTable)):
    createHostTable(hostTable)
if(not checkTable(pingProtocolTable)):
    createProtocolTable(pingProtocolTable)

# check for new hostname and insert
print("Enter new hostnames to store")
hostName = input("Hostname or IP: ") 
if hostName>"":
    addHost(hostTable, hostName)

# list of hosts
hostList = retHosts(hostTable)
for entry in hostList:
    print(entry)