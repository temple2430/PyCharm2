import MySQLdb

# Connect
dba = MySQLdb.connect(host="localhost", user="marco", passwd="root", db="marco2")

mycursor = dba.cursor()

mycursor.execute("DROP DATABASE marco3")