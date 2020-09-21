import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="MyPassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

# sql = "DROP TABLE customers"

# mycursor.execute(sql)

# mydb.commit()

# ###############################
#  DROP Table if exists
#################################

sql = "DROP TABLE IF EXISTS customers"

mycursor.execute(sql)

mydb.commit()