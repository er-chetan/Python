import pymysql

con=pymysql.connect(host='localhost', user='chetan', password='chetan@123', db='db1')
curr=con.cursor()


# name=input("enter your name = ")
# clas=input("enter your class = ")
# roll=input("enter your roll no = ")
# email=input("enter your email = ")
# phoneno=input("enter your phoneno = ")
# address=input("enter your address = ")

# curr.execute(f"insert into student(name,class,rollno,email,phoneno,address) values ('{name}','{clas}','{roll}','{email}','{phoneno}','{address}')")

# con.commit()

# curr.execute("select* from student")

# rows=curr.fetchall()
# print("---------previous data---------")
# for row in rows:
#     print("Name =", row[0],"class =", row[1],"rollno =", row[2],"email =", row[3],"phoneno =", row[4],"address =", row[5])
    

# curr.execute('DELETE FROM student WHERE rollno=34')
# con.commit()
# curr.execute("select* from student")
# rows=curr.fetchall()

# print("---------- after deletion -----------")

# for row in rows:
#     print("Name =", row[0],"class =", row[1],"rollno =", row[2],"email =", row[3],"phoneno =", row[4],"address =", row[5])
    

# print("--------- after update --------- ")

# curr.execute('UPDATE student SET name="rahul" WHERE rollno=44')
# con.commit()

# curr.execute("select* from student")
# rows=curr.fetchall()

# for row in rows:
#     print("Name =", row[0],"class =", row[1],"rollno =", row[2],"email =", row[3],"phoneno =", row[4],"address =", row[5])
    

con.close()
