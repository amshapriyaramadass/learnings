import mysql.connector

mydb = mysql.connector.connect(
    host ="localhost",
    username = "root",
    password="MyPassword",
    database = "mydatabase"
)

mycursor = mydb.cursor()

# #################################
#   ORDER BY
# #################################

# sql = "SELECT * FROM customers ORDER BY name"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

# #################################
#   ORDER BY DESC
# #################################

sql = "SELECT * FROM customers ORDER BY name DESC"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)



