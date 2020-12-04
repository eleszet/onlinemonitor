import psycopg2

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
    return

def createProtocolTable(table):
    conSet = openConnection()
    # create table for protocol entries
    postgreSQL_Query = "create table " + table + " (protocolID SERIAL primary key, hostName VARCHAR (50), protocol VARCHAR (500))"
    conSet[0].execute(postgreSQL_Query, (table,))
    conSet[1].commit()
    closeConnection(conSet)
    return

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
    return

def retHosts(table):
    conSet = openConnection()
    # create table for protocol entries
    postgreSQL_Query = "select hostName from " + table
    conSet[0].execute(postgreSQL_Query)
    lines = conSet[0].fetchall()
    closeConnection(conSet)
    return lines
