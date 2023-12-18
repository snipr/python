# database skills app

import sqlite3
db=sqlite3.connect("skills.db")
cr=db.cursor()
uid=1
cr.execute("CREATE TABLE IF NOT EXISTS skills (s_name TEXT,progress INTEGER,user_id INTEGER)")
def Clos_commit():
    db.commit()
    
    print("the commit is done")

def add_skills():
    skills=input("enter skills name: ")
    prog=input("enter progrss: ")
    cr.execute(f"INSERT INTO skills (s_name,progress,user_id) VALUES ('{skills}',{prog},{uid})")
    Clos_commit()
        
def update_skills():
    
    skills=input("enter skiils name: ")
    prog=input("enter new progrss: ")
    cr.execute(f"UPDATE skills SET progress='{prog}' WHERE s_name='{skills}' AND user_id={uid}")
    Clos_commit()

def delete_skills():
    skills=input("enter skills name: ")
    cr.execute(f"DELETE FROM skills WHERE s_name='{skills}' AND user_id={uid}")
    Clos_commit()

def show_skills():
    cr.execute(f"SELECT * FROM skills WHERE user_id={uid}")
    skills_list=cr.fetchall()
    for skill in skills_list:
        print(f"the skill name => {skill[0]} and progress => {skill[1]}%")
        
    Clos_commit()  

input_massege="""
a => Add new skills
v => View skills
u => Update skills
d => Delete Skills
q => quite app
Chose one option
"""
option_list=["a","v","u","d","q"]
print(input_massege.strip())



option=input("ENTER your Chose: ").strip().lower() 
try: 
  if option in option_list:
    print("the right chouse")
    if option=="a":
       add_skills()
    elif option=="v":
       show_skills()
    elif option=="u":
       update_skills()
    elif option=="d":    
       delete_skills()
    else:
       print("the app end")
       Clos_commit()    
  else:
    raise ValueError
  
except:

    print("wrong choise")        
finally:
  
  db.close()   
  print("DATABASE CLOSED")