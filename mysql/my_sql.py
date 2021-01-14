import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="MohakNasa55055",
    database ="class_8"
)
my_cursor = mydb.cursor()
my_cursor.execute("CREATE TABLE students (roll no INTEGER(40) AUTO-INCREMENT PRIMARY KEY , name VARCHAR(255) , age INTEGER(2) , marks INTEGER(3) )")