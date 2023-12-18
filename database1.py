# DataBase Learn
import sqlite3
#create connection
myList=["Hamza","Ahmed","Rani","Sobheah","Mosa"]
db=sqlite3.connect("app.db")
cr=db.cursor()
#create data base and table 

cr.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER, name TEXT)")

for key,user in enumerate(myList):

    cr.execute(f"INSERT INTO users (user_id,name) VALUES ({key+1},'{user}')")



print("The data base create and the data inserted")

db.commit()
db.close()

