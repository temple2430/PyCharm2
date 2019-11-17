import MySQLdb

# Connect
dba = MySQLdb.connect(host="localhost", user="marco", passwd="root", db="marco")

mycursor = dba.cursor()

mycursor.execute("CREATE DATABASE marco3")