import mysql.connector
import pyttsx3

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "Rithic@2002",
	database = "username_password"
	)
mycursor = mydb.cursor()

def Retrive(retrive_method):
	mycursor.execute("SELECT * FROM user_details")
	result = mycursor.fetchall()
	if retrive_method == "sitename":
		retrive_value = input("Enter the name of the"+" "+retrive_method)
		for i in result:
			if retrive_value == i[0] :
				print("The sitename is"+" "+i[0])
				pyttsx3.speak(i[0])
				print("The username is"+" "+i[1])
				pyttsx3.speak(i[1])
				print("The password is"+" "+i[2])
				pyttsx3.speak(i[2])
			
	elif retrive_method == "username":
 		retrive_value = input("Enter the name of the"+" "+retrive_method)
 		for i in result:
 			if retrive_value == i[1] :
 				print("The sitename is"+" "+i[0])
 				pyttsx3.speak(i[0])
 				print("The username is"+" "+i[1])
 				pyttsx3.speak(i[1])
 				print("The password is"+" "+i[2])
 				pyttsx3.speak(i[2])

def Update(update_method):
	return update_method

def Remove(remove_method):
	return remove_method

def Add():
	site = input("Enter the sitename")
	user = input("Enter the username")
	passwd = input("Enter the password")
	sql = "INSERT INTO user_details(site_name,username,password) VALUES(%s, %s, %s)"
	values = (site, user, passwd)
	mycursor.execute(sql,values)
	mydb.commit()
	print("The commit was sucessfully made")
	return 0



text = "Hello! Welcome the search and retrive username password Centre. How can I help You?"
pyttsx3.speak(text)

what = input("Retrive/Update/Remove/Add")
if what == "Retrive":
	retrive_method = input("Meathod to retrive the details of user by site_name or username")
	Retrive(retrive_method)

elif what =="Update":
	update_method = input("Meathod to update the details of user site_name or username or password")
	Update(update_method)

elif what == "Remove":
	remove_method = input("Meathod to remove the details of user by site_name or username or password")
	Remove(remove_method)
elif what == "Add":
	#add_method = input("Meathod to remove the details of user by site_name or username or password")
	Add()

else:
	print("No commands found")
