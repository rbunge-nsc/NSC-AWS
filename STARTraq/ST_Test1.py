#print("Hello World!")
print("Good-bye World!")

#fname = input("Enter your file name: ") 
#msg = input("Enter your message: ")

#f = open("/home/ec2-user/environment/NSC-AWS/STARTraq/ {} .txt".format(fname), "x")
#f.write(msg)
#f.close()

#f = open("/home/ec2-user/environment/NSC-AWS/STARTraq/ {} .txt".format(fname), "r")
#print(f.read())
#f.close()


#>>> shepherd = "Mary"
#>>> age = 32
#>>> stuff_in_string = "Shepherd {} is {} years old.".format(shepherd, age)

# importing the module
#import MySQLdb



import mysql.connector
from mysql.connector import Error

# opening a database connection
connection = mysql.connector.connect(
    host = 'database-1-instance-1.ctv9cnkyburi.us-east-1.rds.amazonaws.com',
    database = 'testDB',
    user = 'admin',
    password = 'password')

# define a cursor object
cursor = connection.cursor()

# drop table if exists
#cursor.execute("IF STUDENT TABLE EXISTS DROP IT")

cursor.execute("SELECT * FROM Persons")

for x in cursor:
  print(x)

# query
#sql = "INSERT INTO Persons (LastName, FirstName) VALUES (%s, %s)"
#val = ("Jones", "Jon")
#cursor.execute(sql, val)

# execute query
#cursor.execute(sql)

# close object
cursor.close()

# close connection
connection.close()