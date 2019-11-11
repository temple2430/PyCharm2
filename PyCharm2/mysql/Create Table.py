import MySQLdb

# Connect
dba = MySQLdb.connect(host="localhost", user="marco", passwd="root", db="marco")

mycursor = dba.cursor()


mycursor.execute("CREATE TABLE Suppliers (ID VARCHAR(50), Name VARCHAR(50),Supplier VARCHAR(50), Address Varchar(50))")

dba.commit()
