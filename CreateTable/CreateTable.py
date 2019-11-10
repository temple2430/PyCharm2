import MySQLdb

# Connect
dba = MySQLdb.connect(host="localhost", user="marco", passwd="root", db="worls")

mycursor = dba.cursor()


mycursor.execute("CREATE TABLE Product (ID VARCHAR(50), Price VARCHAR(50),Supplier VARCHAR(50), Quantity Varchar(50))")

