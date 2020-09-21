import mysql.connector

mydb = mysql.connector.connect(
    host ="localhost",
    username ="root",
    password="MyPassword",
    database = "mydatabase"
)

# mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM customers")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)


# ################################
# Selecting coloumns
# ############################
# mycursor = mydb.cursor()

# mycursor.execute("SELECT name, address FROM customers")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x) 

# ##########################
# Use FEtchone Method 
# ####################

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()

print(myresult)  
