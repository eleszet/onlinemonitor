import psycopg2
import datetime

hostTable = "hostnames"
protocolTable = "protocol"


def checkExists():  # check if tables exist, if not create
    if(not checkTable(hostTable)):
        createHostTable()
    if(not checkTable(protocolTable)):
        createProtocolTable()


def checkTable(table):  # function to check if a table is existing
    # 0=cursor, 1=connection
    conSet = openConnection()
    # select target table and check if it's available or not
    postgreSQL_Query = "SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = %s)"
    conSet[0].execute(postgreSQL_Query, (table,))
    # read return value
    lines = conSet[0].fetchall()
    for row in lines:
        rVal = (row[0])
    # close connection
    closeConnection(conSet)
    # return value
    if(str(rVal).upper() == "FALSE"):
        return False
    else:
        return True


def createHostTable():
    conSet = openConnection()
    # create table for host entries
    postgreSQL_Query = "create table " + hostTable + \
        " (hostName VARCHAR (50) primary key, hostIP VARCHAR (50))"
    conSet[0].execute(postgreSQL_Query, (hostTable,))
    conSet[1].commit()
    closeConnection(conSet)


def createProtocolTable():
    conSet = openConnection()
    # create table for protocol entries
    postgreSQL_Query = "create table " + protocolTable + \
        " (protocolID SERIAL primary key, hostName VARCHAR (50), reaction decimal(10,2), issue varchar(1), date_added timestamp default NULL)"
    conSet[0].execute(postgreSQL_Query, (protocolTable,))
    conSet[1].commit()
    closeConnection(conSet)


def openConnection():
    connection = psycopg2.connect(
        host="localhost",
        port="5432",
        database="",
        user="postgres",
        password="postgres")
    cursor = connection.cursor()
    return [cursor, connection]


def closeConnection(conSet):
    conSet[0].close()
    conSet[1].close()


def addHost(hostName):
    conSet = openConnection()
    # create table for protocol entries
    postgreSQL_Query = "insert into " + hostTable + " (hostName) values(%s)"
    try:
        conSet[0].execute(postgreSQL_Query, (hostName,))
        conSet[1].commit()
    except:
        print("Error while saving")
    closeConnection(conSet)


def rmHost(hostName):
    conSet = openConnection()
    # create table for protocol entries
    postgreSQL_Query = "delete from " + hostTable + " where  hostName = %s"
    try:
        conSet[0].execute(postgreSQL_Query, (hostName,))
        conSet[1].commit()
    except:
        print("Error while saving")
    closeConnection(conSet)


def addProtocol(hostName, ms, issue):
    conSet = openConnection()
    # create table for protocol entries
    postgreSQL_Query = "insert into " + protocolTable + \
        " (hostName, reaction, issue, date_added) values(%s, %s, %s, %s)"
    try:
        conSet[0].execute(postgreSQL_Query, (hostName, ms,
                                             issue, datetime.datetime.now(),))
        conSet[1].commit()
    except:
        print("Error while saving")
    closeConnection(conSet)


def retHosts():
    conSet = openConnection()
    # create table for protocol entries
    postgreSQL_Query = "select hostName from " + hostTable
    conSet[0].execute(postgreSQL_Query)
    lines = conSet[0].fetchall()
    closeConnection(conSet)
    return lines


def retAll10():
    conSet = openConnection()
    # create table for protocol entries
    postgreSQL_Query = "select hostname, avg(reaction), count(*), count(issue) filter (where issue ='1'), count(issue) filter (where issue ='0') from " + \
        protocolTable + " org where date_added > %s group by hostname "
    conSet[0].execute(postgreSQL_Query, (getFromTime(),))
    lines = conSet[0].fetchall()
    closeConnection(conSet)
    return lines


def getFromTime():
    timeDifferenceMinutes = 15
    return datetime.datetime.now() - datetime.timedelta(minutes=timeDifferenceMinutes)
