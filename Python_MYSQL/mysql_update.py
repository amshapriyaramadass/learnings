import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="MyPassword",
  database="mydatabase"
)

mycursor = mydb.cursor()
# ##########################
# Update TAble 
##############################

# sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "record(s) affected")

# #################################
#  Prevent SQL Injection
##################################
sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")




