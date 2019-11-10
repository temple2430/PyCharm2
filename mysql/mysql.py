import MySQLdb

# Connect
db = MySQLdb.connect(host="localhost", user="marco", passwd="root", db="marco")

mycursor = db.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [("James", "Glasgow"),
       ("John3", "Edinburgh"),
       ("Mark", "Dingwall"),
       ("David","Aberdeen")]
mycursor.executemany(sql, val)

db.commit()
print("Data Saved")

#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
#my_cursor.execute("SELECT * FROM city")

#my_result = my_cursor.fetchall()

# for x in my_result:
#   print(x)