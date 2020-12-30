import mysql.connector
mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "Rithic@2002",
	database = "username_password"
	)

mycursor = mydb.cursor()

inp = input("Enter the way you want to search your usename and password")
x = input("Enter the"+" "+inp+" "+"you want to querry on")
sql = "SELECT * FROM user_details "
mycursor.execute(sql)
x1 = mycursor.fetchall()
if inp =="site_name":
	for i in x1:
		if i[0]==x:
			print(i)
elif inp =="username":
	for i in x1:
		if i[1]==x:
			print(i)
elif inp =="password":
	for i in x1:
		if i[2]==x:
			print(i)


