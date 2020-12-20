import psycopg2
import datetime

# class to check if a table is existing
def checkTable(table):
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
    if(str(rVal).upper()=="FALSE") :
        return False  
    else:
        return True

def createHostTable(table):
    conSet = openConnection()
    # create table for host entries
    postgreSQL_Query = "create table " + table + " (hostName VARCHAR (50) primary key, hostIP VARCHAR (50))"
    conSet[0].execute(postgreSQL_Query, (table,))
    conSet[1].commit()
    closeConnection(conSet)

def createProtocolTable(table):
    conSet = openConnection()
    # create table for protocol entries
    postgreSQL_Query = "create table " + table + " (protocolID SERIAL primary key, hostName VARCHAR (50), reaction decimal(10,2), issue varchar(1), date_added timestamp default NULL)"
    conSet[0].execute(postgreSQL_Query, (table,))
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

def addHost(table, hostName):
    conSet = openConnection()
    # create table for protocol entries
    postgreSQL_Query = "insert into " + table + " (hostName) values(%s)"
    try:
        conSet[0].execute(postgreSQL_Query, (hostName,))
        conSet[1].commit()
    except:
        print("Error while saving")
    closeConnection(conSet)
    
def addProtocol(table, hostName, ms, issue):
    conSet = openConnection()
    # create table for protocol entries
    postgreSQL_Query = "insert into " + table + " (hostName, reaction, issue, date_added) values(%s, %s, %s, %s)"
    try:
        conSet[0].execute(postgreSQL_Query, (hostName, ms, issue, datetime.datetime.now(),))
        conSet[1].commit()
    except:
        print("Error while saving")
    closeConnection(conSet)

def retHosts(table):
    conSet = openConnection()
    # create table for protocol entries
    postgreSQL_Query = "select hostName from " + table
    conSet[0].execute(postgreSQL_Query)
    lines = conSet[0].fetchall()
    closeConnection(conSet)
    return lines

def retAll10(table):
    conSet = openConnection()
    # create table for protocol entries
    postgreSQL_Query = "select hostname, avg(reaction), count(*), count(issue) filter (where issue ='1'), count(issue) filter (where issue ='0') from " + table + " org where date_added > %s group by hostname "
    conSet[0].execute(postgreSQL_Query, (getFromTime(),))
    lines = conSet[0].fetchall()
    closeConnection(conSet)
    return lines

def retHostInfo10(table, hostName):
    conSet = openConnection()
    # create table for protocol entries
    postgreSQL_Query = "select hostName, avg(reaction) from " + table + " org where hostname = %s and date_added > %s group by hostname"
    conSet[0].execute(postgreSQL_Query, (hostName,getFromTime(),))
    lines = conSet[0].fetchall()
    closeConnection(conSet)
    return lines
    
def countTotalForHost10(table, hostName):
    conSet = openConnection()
    # create table for protocol entries
    postgreSQL_Query = "select count(*) from " + table + " org where hostname = %s and date_added > %s"
    conSet[0].execute(postgreSQL_Query, (hostName,getFromTime(),))
    lines = conSet[0].fetchall()
    closeConnection(conSet)
    return lines

def countIssueHost10(table, hostName, failSucess):
    conSet = openConnection()
    # create table for protocol entries
    postgreSQL_Query = "select count(*) from " + table + " org where hostname = %s and date_added > %s and issue=%s"
    conSet[0].execute(postgreSQL_Query, (hostName,getFromTime(), failSucess,))
    lines = conSet[0].fetchall()
    closeConnection(conSet)
    return lines

def countTotalForAll10(table):
    conSet = openConnection()
    # create table for protocol entries
    postgreSQL_Query = "select count(*) from " + table + " org where date_added > %s"
    conSet[0].execute(postgreSQL_Query, (getFromTime(),))
    lines = conSet[0].fetchall()
    closeConnection(conSet)
    return lines

def getFromTime():
    timeDifferenceMinutes = 15
    return datetime.datetime.now() - datetime.timedelta(minutes=timeDifferenceMinutes)
