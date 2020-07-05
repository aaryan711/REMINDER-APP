import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

if __name__=="__main__":
    print(mydb)
    cr=mydb.cursor()
    try:
        cr.execute("CREATE DATABASE mydatabase")
        print "DATABASE CREATED!!!"
    except:
        print "DATABASE already exist!!!"
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="mydatabase")
        cr = mydb.cursor()
        cr.execute("CREATE TABLE reminder (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255) , message VARCHAR(255))")
        cr.execute("SHOW TABLES")
        for table in cr:
            print (table)
        print ("TABLE CREATED!!!")
    except:
        print "TABLE already exist Proceed further!!!"
    exitapp=True
    while exitapp:
        print("Enter your choise in numbers")
        print("""1.create a reminder
2.update a reminder
3.view reminder
4.Exit application""")
        num=input()
        if(num==1):
            title=raw_input("write something")
            message=raw_input("discribe your task")
            sql="INSERT INTO reminder (title,message) VALUES (%s,%s)"
            val=(title,message)
            cr.execute(sql,val)
            mydb.commit()
            print(cr.rowcount,"Reminder added!!!")
        elif(num==2):
            cr.execute("SELECT * FROM reminder")
            result = cr.fetchall()
            print("select the Id of reminder that you want to update")
            print(result)
            rid=raw_input("Enter the ID")
            newtitle=raw_input("Enter new title")
            newmsg=raw_input("Enter new message")
            updatesql= "UPDATE reminder SET title = %s,message = %s WHERE id = %s"
            updateval=(newtitle,newmsg,rid)
            cr.execute(updatesql,updateval)
            mydb.commit()
            print(cr.rowcount,"Reminder updated")
        elif(num==3):
            print("here is list of all the reminders")
            cr.execute("SELECT * FROM reminder")
            result = cr.fetchall()
            print(result)
        elif(num==4):
            exitapp=False
        else:
            print("wrong choise")
