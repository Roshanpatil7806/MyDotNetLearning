import mysql.connector
# Connect to MySQL
dbConnection = mysql.connector.connect(host="localhost", user="root",  password="Roshan@9014", database="office")

dbCommand = dbConnection.cursor()

def  get_employee():
    dbCommand.execute("SELECT * FROM employee")
    result = dbCommand.fetchall()
    for row in result:
        print(row)


# DELETE
def delete_employee():
    emp_id = int(input("Enter ID: "))
    sql = "DELETE FROM employee WHERE ID=%s"   #Query
    dbCommand.execute(sql, (emp_id,))
    dbConnection.commit()
    print("employee deleted successfully")


# CREATE
def add_employee():
    emp_id = int(input("Enter ID: "))
    emp_name = input("Enter Name: ")
    emp_email = input("Enter Email: ")

    sql = "INSERT INTO employee (emp_id, emp_name, emp_email) VALUES (%s, %s, %s)"
    values = (emp_id, emp_name, emp_email)

    dbCommand.execute(sql, values)
    dbConnection.commit()
    print("employee added successfully")


# UPDATE
def update_employee():
    emp_id = int(input("Enter ID: "))
    emp_name = input("Enter new Name: ")
    emp_email = input("Enter new Email: ")

    sql = "UPDATE employee SET emp_name=%s, emp_email=%s WHERE emp_id=%s"
    values = (emp_name, emp_email, emp_id)

    dbCommand.execute(sql, values)
    dbConnection.commit()

    print("employee updated successfully")


#menu


while True:
    print("\n1. Add employee")
    print("2. Show employee")
    print("3. Update employee")
    print("4. Delete employee")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_employeet()

    elif choice == "2":
        get_employee()

    elif choice == "3":
        update_employee()

    elif choice == "4":
        delete_employee()

    elif choice == "5":
        break

    else:
        print("Invalid choice")

dbCommand.close()
dbConnection.close()



# Data Layer: MySQL database connection 
#             Creating database, inerting sample data,
#             Testing database using SQL commands, Join queires and Stored procedure 
#             from the prespective of DBA

# DAL "Data Access Layer"
#            from the perspective of a developer,
#            we will create a python application to connect to the database and
#            perform CRUD operations on the database