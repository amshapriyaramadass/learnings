import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="MyPassword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")


# ########################
# Check DB exists
#######################
# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#   print(x)