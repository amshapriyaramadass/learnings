import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    username = "root",
    password = "MyPassword",
    database = "mydatabase"
)

mycursor = mydb.cursor()

# #################################
#  DELECT RECORD 
###################################

# sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "record(s) deleted")

# ###################################
#  Prevent SQL injecton
# ###################################

sql ="DELETE FROM customers WHERE address = %s"

adr = ("Yellow Garden 2", )
mycursor.execute(sql,adr)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")

