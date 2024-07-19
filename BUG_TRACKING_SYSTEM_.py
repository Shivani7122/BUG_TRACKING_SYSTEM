import pymysql

def setup_database():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='sql',
        database='BDS',
        charset='utf8'
    )
    
    cursor = connection.cursor()
    
    # Create Employee Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Employee (
                        empCode INT PRIMARY KEY,
                        empName VARCHAR(30),
                        empEmail VARCHAR(40),
                        empPassword VARCHAR(20),
                        gender VARCHAR(10),
                        DOB VARCHAR(20),
                        mobileNo BIGINT,
                        Role VARCHAR(20)
                      )''')

    # Create AssignProject Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS AssignProject (
                        projectID INT,
                        empCode INT,
                        FOREIGN KEY (projectID) REFERENCES Project(projectID),
                        FOREIGN KEY (empCode) REFERENCES Employee(empCode)
                      )''')

    # Create Project Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Project (
                        projectID INT PRIMARY KEY,
                        projectName VARCHAR(30),
                        SDate VARCHAR(30),
                        EDate VARCHAR(30),
                        projectDec VARCHAR(200)
                      )''')

    # Create BugReport Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS BugReport (
                        bugNo INT PRIMARY KEY,
                        bugCode INT,
                        projectID INT,
                        TCode INT,
                        ECode INT,
                        status VARCHAR(20),
                        bugDes VARCHAR(100),
                        FOREIGN KEY (bugCode) REFERENCES BugType(bugCode),
                        FOREIGN KEY (projectID) REFERENCES Project(projectID),
                        FOREIGN KEY (TCode) REFERENCES Employee(empCode),
                        FOREIGN KEY (ECode) REFERENCES Employee(empCode)
                      )''')

    # Create BugType Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS BugType (
                        bugCode INT PRIMARY KEY,
                        bugCatgory VARCHAR(30),
                        bugSeverty VARCHAR(20)
                      )''')

    connection.commit()
    connection.close()

setup_database()

def admin_module():
    while True:
        print("\nAdmin Panel")
        print("1. Manager")
        print("2. Employee")
        print("3. View All Projects")
        print("4. View Bug Reports")
        print("5. Insert into Projects")
        print("6. Insert into Bug Reports")
        print("7. Go to User Login")
        print("8. Exit ")
        
        choice = input("Enter choice: ")

        if choice == '1':
            admin_manager()
        elif choice == '2':
            admin_employee()
        elif choice == '3':
            view_all_projects()
        elif choice == '4':
            view_bug_reports()
        elif choice == '5':
            add_project()
        elif choice == '6':
            add_new_bug()
        elif choice == '7':
            user_login()
        elif choice == '8':
            break
        else:
            print("Invalid choice! Please try again.")

def admin_manager():
    while True:
        print("\nManager Panel")
        print("1. Add Manager Account")
        print("2. View Manager Account")
        print("3. Delete Manager")
        print("4. Update Manager Details")
        print("5. Back")
        
        choice = input("Enter choice: ")

        if choice == '1':
            add_manager_account()
        elif choice == '2':
            view_manager_account()
        elif choice == '3':
            delete_manager()
        elif choice == '4':
            update_manager_details()
        elif choice == '5':
            break
        else:
            print("Invalid choice! Please try again.")

def add_manager_account():
    empCode = int(input("Enter Manager Code: "))
    empName = input("Enter Manager Name: ")
    empEmail = input("Enter Manager Email: ")
    empPassword = input("Enter Manager Password: ")
    gender = input("Enter Gender: ")
    DOB = input("Enter Date of Birth: ")
    mobileNo = int(input("Enter Mobile Number: "))
    Role = "Manager"
    
    connection = pymysql.connect(host='localhost', user='root', password='sql', database='BDS', charset='utf8')
    cursor = connection.cursor()
    
    cursor.execute("INSERT INTO Employee (empCode, empName, empEmail, empPassword, gender, DOB, mobileNo, Role) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                   (empCode, empName, empEmail, empPassword, gender, DOB, mobileNo, Role))
    
    connection.commit()
    connection.close()
    print("Manager account added successfully.")

def view_manager_account():
    connection = pymysql.connect(host='localhost', user='root', password='sql', database='BDS', charset='utf8')
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM Employee WHERE Role='Manager'")
    results = cursor.fetchall()
    
    for row in results:
        print(row)
    
    connection.close()

def delete_manager():
    empCode = int(input("Enter Manager Code to delete: "))
    
    connection = pymysql.connect(host='localhost', user='root', password='sql', database='BDS', charset='utf8')
    cursor = connection.cursor()
    
    cursor.execute("DELETE FROM Employee WHERE empCode=%s AND Role='Manager'", (empCode,))
    
    connection.commit()
    connection.close()
    print("Manager deleted successfully.")

def update_manager_details():
    empCode = int(input("Enter Manager Code to update: "))
    empName = input("Enter new Name: ")
    empEmail = input("Enter new Email: ")
    empPassword = input("Enter new Password: ")
    gender = input("Enter new Gender: ")
    DOB = input("Enter new Date of Birth: ")
    mobileNo = int(input("Enter new Mobile Number: "))
    
    connection = pymysql.connect(host='localhost', user='root', password='sql', database='BDS', charset='utf8')
    cursor = connection.cursor()
    
    cursor.execute("UPDATE Employee SET empName=%s, empEmail=%s, empPassword=%s, gender=%s, DOB=%s, mobileNo=%s WHERE empCode=%s AND Role='Manager'",
                   (empName, empEmail, empPassword, gender, DOB, mobileNo, empCode))
    
    connection.commit()
    connection.close()
    print("Manager details updated successfully.")

def admin_employee():
    while True:
        print("\nEmployee Panel")
        print("1. Add Employee Account")
        print("2. View Employee Account")
        print("3. Delete Employee Account")
        print("4. Update Employee Details")
        print("5. Back")
        
        choice = input("Enter choice: ")

        if choice == '1':
            add_employee_account()
        elif choice == '2':
            view_employee_account()
        elif choice == '3':
            delete_employee_account()
        elif choice == '4':
            update_employee_details()
        elif choice == '5':
            break
        else:
            print("Invalid choice! Please try again.")

def add_employee_account():
    empCode = int(input("Enter Employee Code: "))
    empName = input("Enter Employee Name: ")
    empEmail = input("Enter Employee Email: ")
    empPassword = input("Enter Employee Password: ")
    gender = input("Enter Gender: ")
    DOB = input("Enter Date of Birth: ")
    mobileNo = int(input("Enter Mobile Number: "))
    Role = "Employee"
    
    connection = pymysql.connect(host='localhost', user='root', password='sql', database='BDS', charset='utf8')
    cursor = connection.cursor()
    
    cursor.execute("INSERT INTO Employee (empCode, empName, empEmail, empPassword, gender, DOB, mobileNo, Role) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                   (empCode, empName, empEmail, empPassword, gender, DOB, mobileNo, Role))
    
    connection.commit()
    connection.close()
    print("Employee account added successfully.")

def view_employee_account():
    connection = pymysql.connect(host='localhost', user='root', password='sql', database='BDS', charset='utf8')
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM Employee WHERE Role='Employee'")
    results = cursor.fetchall()
    
    for row in results:
        print(row)
    
    connection.close()

def delete_employee_account():
    empCode = int(input("Enter Employee Code to delete: "))
    
    connection = pymysql.connect(host='localhost', user='root', password='sql', database='BDS', charset='utf8')
    cursor = connection.cursor()
    
    cursor.execute("DELETE FROM Employee WHERE empCode=%s AND Role='Employee'", (empCode,))
    
    connection.commit()
    connection.close()
    print("Employee deleted successfully.")

def update_employee_details():
    empCode = int(input("Enter Employee Code to update: "))
    empName = input("Enter new Name: ")
    empEmail = input("Enter new Email: ")
    empPassword = input("Enter new Password: ")
    gender = input("Enter new Gender: ")
    DOB = input("Enter new Date of Birth: ")
    mobileNo = int(input("Enter new Mobile Number: "))
    
    connection = pymysql.connect(host='localhost', user='root', password='sql', database='BDS', charset='utf8')
    cursor = connection.cursor()
    
    cursor.execute("UPDATE Employee SET empName=%s, empEmail=%s, empPassword=%s, gender=%s, DOB=%s, mobileNo=%s WHERE empCode=%s AND Role='Employee'",
                   (empName, empEmail, empPassword, gender, DOB, mobileNo, empCode))
    
    connection.commit()
    connection.close()
    print("Employee details updated successfully.")

def view_all_projects():
    connection = pymysql.connect(host='localhost', user='root', password='sql', database='BDS', charset='utf8')
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM Project")
    results = cursor.fetchall()
    
    for row in results:
        print(row)
    
    connection.close()

def view_bug_reports():
    connection = pymysql.connect(host='localhost', user='root', password='sql', database='BDS', charset='utf8')
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM BugReport")
    results = cursor.fetchall()
    
    for row in results:
        print(row)
    
    connection.close()

def add_project():
    projectID = int(input("Enter Project ID: "))
    projectName = input("Enter Project Name: ")
    SDate = input("Enter Start Date: ")
    EDate = input("Enter End Date: ")
    projectDec = input("Enter Project Description: ")
    
    connection = pymysql.connect(host='localhost', user='root', password='sql', database='BDS', charset='utf8')
    cursor = connection.cursor()
    
    cursor.execute("INSERT INTO Project (projectID, projectName, SDate, EDate, projectDec) VALUES (%s, %s, %s, %s, %s)",
                   (projectID, projectName, SDate, EDate, projectDec))
    
    connection.commit()
    connection.close()
    print("Project added successfully.")

def add_new_bug():
    bugNo = int(input("Enter Bug Number: "))
    bugCode = int(input("Enter Bug Code: "))
    projectID = int(input("Enter Project ID: "))
    TCode = int(input("Enter Tester Code: "))
    ECode = int(input("Enter Engineer Code: "))
    status = input("Enter Bug Status: ")
    bugDes = input("Enter Bug Description: ")
    
    connection = pymysql.connect(host='localhost', user='root', password='sql', database='BDS', charset='utf8')
    cursor = connection.cursor()
    
    cursor.execute("INSERT INTO BugReport (bugNo, bugCode, projectID, TCode, ECode, status, bugDes) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   (bugNo, bugCode, projectID, TCode, ECode, status, bugDes))
    
    connection.commit()
    connection.close()
    print("Bug report added successfully.")

def manager_module():
    while True:
        print("\nManager Panel")
        print("1. Update Profile")
        print("2. Manage Projects")
        print("3. Bugs")
        print("4. Exit")
        
        choice = input("Enter choice: ")

        if choice == '1':
            update_profile()
        elif choice == '2':
            manage_projects()
        elif choice == '3':
            manage_bugs()
        elif choice == '4':
            break
        else:
            print("Invalid choice! Please try again.")

def manage_projects():
    while True:
        print("\nManage Projects")
        print("1. Add Project")
        print("2. View All Projects")
        print("3. Delete Project")
        print("4. Update Project")
        print("5. Back")
        
        choice = input("Enter choice: ")

        if choice == '1':
            add_project()
        elif choice == '2':
            view_all_projects()
        elif choice == '3':
            delete_project()
        elif choice == '4':
            update_project()
        elif choice == '5':
            break
        else:
            print("Invalid choice! Please try again.")

def manage_bugs():
    while True:
        print("\nManage Bugs")
        print("1. Add New Bug")
        print("2. View All Bugs")
        print("3. Update Bug")
        print("4. Delete Bug")
        print("5. Back")
        
        choice = input("Enter choice: ")

        if choice == '1':
            add_new_bug()
        elif choice == '2':
            view_all_bugs()
        elif choice == '3':
            update_bug()
        elif choice == '4':
            delete_bug()
        elif choice == '5':
            break
        else:
            print("Invalid choice! Please try again.")

def update_profile():
    empCode = int(input("Enter your Employee Code: "))
    empName = input("Enter new Name: ")
    empEmail = input("Enter new Email: ")
    empPassword = input("Enter new Password: ")
    gender = input("Enter new Gender: ")
    DOB = input("Enter new Date of Birth: ")
    mobileNo = int(input("Enter new Mobile Number: "))
    
    connection = pymysql.connect(host='localhost', user='root', password='sql', database='BDS', charset='utf8')
    cursor = connection.cursor()
    
    cursor.execute("UPDATE Employee SET empName=%s, empEmail=%s, empPassword=%s, gender=%s, DOB=%s, mobileNo=%s WHERE empCode=%s",
                   (empName, empEmail, empPassword, gender, DOB, mobileNo, empCode))
    
    connection.commit()
    connection.close()
    print("Profile updated successfully.")

def delete_project():
    projectID = int(input("Enter Project ID to delete: "))
    
    connection = pymysql.connect(host='localhost', user='root', password='sql', database='BDS', charset='utf8')
    cursor = connection.cursor()
    
    cursor.execute("DELETE FROM Project WHERE projectID=%s", (projectID,))
    
    connection.commit()
    connection.close()
    print("Project deleted successfully.")

def update_project():
    projectID = int(input("Enter Project ID to update: "))
    projectName = input("Enter new Project Name: ")
    SDate = input("Enter new Start Date: ")
    EDate = input("Enter new End Date: ")
    projectDec = input("Enter new Project Description: ")
    
    connection = pymysql.connect(host='localhost', user='root', password='sql', database='BDS', charset='utf8')
    cursor = connection.cursor()
    
    cursor.execute("UPDATE Project SET projectName=%s, SDate=%s, EDate=%s, projectDec=%s WHERE projectID=%s",
                   (projectName, SDate, EDate, projectDec, projectID))
    
    connection.commit()
    connection.close()
    print("Project updated successfully.")

def view_all_bugs():
    connection = pymysql.connect(host='localhost', user='root', password='sql', database='BDS', charset='utf8')
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM BugReport")
    results = cursor.fetchall()
    
    for row in results:
        print(row)
    
    connection.close()

def update_bug():
    bugNo = int(input("Enter Bug Number to update: "))
    bugCode = int(input("Enter new Bug Code: "))
    projectID = int(input("Enter new Project ID: "))
    TCode = int(input("Enter new Tester Code: "))
    ECode = int(input("Enter new Engineer Code: "))
    status = input("Enter new Bug Status: ")
    bugDes = input("Enter new Bug Description: ")
    
    connection = pymysql.connect(host='localhost', user='root', password='sql', database='BDS', charset='utf8')
    cursor = connection.cursor()
    
    cursor.execute("UPDATE BugReport SET bugCode=%s, projectID=%s, TCode=%s, ECode=%s, status=%s, bugDes=%s WHERE bugNo=%s",
                   (bugCode, projectID, TCode, ECode, status, bugDes, bugNo))
    
    connection.commit()
    connection.close()
    print("Bug updated successfully.")

def delete_bug():
    bugNo = int(input("Enter Bug Number to delete: "))
    
    connection = pymysql.connect(host='localhost', user='root', password='sql', database='BDS', charset='utf8')
    cursor = connection.cursor()
    
    cursor.execute("DELETE FROM BugReport WHERE bugNo=%s", (bugNo,))
    
    connection.commit()
    connection.close()
    print("Bug deleted successfully.")

def employee_module():
    while True:
        print("\nEmployee Panel")
        print("1. Update Profile")
        print("2. Add Bug's Report")
        print("3. Update Bug Status")
        print("4. View Bugs")
        print("5. Bug Details")
        print("6. Exit")
        
        choice = input("Enter choice: ")

        if choice == '1':
            update_profile()
        elif choice == '2':
            add_bug_report()
        elif choice == '3':
            update_bug_status()
        elif choice == '4':
            view_bugs()
        elif choice == '5':
            bug_details()
        elif choice == '6':
            break
        else:
            print("Invalid choice! Please try again.")

def add_bug_report():
    bugNo = int(input("Enter Bug Number: "))
    bugCode = int(input("Enter Bug Code: "))
    projectID = int(input("Enter Project ID: "))
    TCode = int(input("Enter Tester Code: "))
    ECode = int(input("Enter Engineer Code: "))
    status = input("Enter Bug Status: ")
    bugDes = input("Enter Bug Description: ")
    
    connection = pymysql.connect(host='localhost', user='root', password='sql', database='BDS', charset='utf8')
    cursor = connection.cursor()
    
    cursor.execute("INSERT INTO BugReport (bugNo, bugCode, projectID, TCode, ECode, status, bugDes) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   (bugNo, bugCode, projectID, TCode, ECode, status, bugDes))
    
    connection.commit()
    connection.close()
    print("Bug report added successfully.")

def update_bug_status():
    bugNo = int(input("Enter Bug Number to update status: "))
    status = input("Enter new Bug Status: ")
    
    connection = pymysql.connect(host='localhost', user='root', password='sql', database='BDS', charset='utf8')
    cursor = connection.cursor()
    
    cursor.execute("UPDATE BugReport SET status=%s WHERE bugNo=%s", (status, bugNo))
    
    connection.commit()
    connection.close()
    print("Bug status updated successfully.")

def view_bugs():
    connection = pymysql.connect(host='localhost', user='root', password='sql', database='BDS', charset='utf8')
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM BugReport")
    results = cursor.fetchall()
    
    for row in results:
        print(row)
    
    connection.close()

def bug_details():
    bugNo = int(input("Enter Bug Number to view details: "))
    
    connection = pymysql.connect(host='localhost', user='root', password='sql', database='BDS', charset='utf8')
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM BugReport WHERE bugNo=%s", (bugNo,))
    result = cursor.fetchone()
    
    if result:
        print(result)
    else:
        print("No bug found with the given number.")
    
    connection.close()


def admin_login():
    admin_email = input("Enter Admin Email: ")
    admin_password = input("Enter Admin Password: ")
    
    if admin_email == 'admin@example.com' and admin_password == 'admin123':
        admin_module()
    else:
        print("Invalid admin credentials!")

def manager_login():
    empEmail = input("Enter Manager Email: ")
    empPassword = input("Enter Manager Password: ")
    
    connection = pymysql.connect(host='localhost', user='root', password='sql', database='BDS', charset='utf8')
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM Employee WHERE empEmail=%s AND empPassword=%s AND Role='Manager'", (empEmail, empPassword))
    result = cursor.fetchone()
    
    connection.close()
    
    if result:
        manager_module()
    else:
        print("Invalid manager credentials!")

def employee_login():
    empEmail = input("Enter Employee Email: ")
    empPassword = input("Enter Employee Password: ")
    
    connection = pymysql.connect(host='localhost', user='root', password='sql', database='BDS', charset='utf8')
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM Employee WHERE empEmail=%s AND empPassword=%s AND Role='Employee'", (empEmail, empPassword))
    result = cursor.fetchone()
    
    connection.close()
    
    if result:
        employee_module()
    else:
        print("Invalid employee credentials!")

def user_login():
    while True:
        print("\nUser Login")
        print("1. Admin Login")
        print("2. Manager Login")
        print("3. Employee Login")
        print("4. Exit")
        
        choice = input("Enter choice: ")

        if choice == '1':
            admin_login()
        elif choice == '2':
            manager_login()
        elif choice == '3':
            employee_login()
        elif choice == '4':
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == '__main__':
    setup_database()
    admin_module()
    
