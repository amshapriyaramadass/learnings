import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="MyPassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# ####################################
#  Check TAble EXists
#######################################
# show table 
# mycursor.execute("SHOW TABLES ")

# for x in mycursor:
#     print(x)

# ##################################
#  Create table with Primary Key 
####################################
# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

##########################
#  Alter Table 
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
