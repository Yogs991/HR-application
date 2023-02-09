import mysql.connector
con=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='hr'
)

cur=con.cursor()

class Employee:
    def __innit__(self,name,email,phone,address,salary):
        self.id= 0
        self.name=name
        self.email=email
        self.phone=phone
        self.address=address
        self.salary=salary


#Προσθηκη υπαλληλου στην βαση
    def add_emp(self):
        ask = 'Y'
        list_ids = check()
        while ask in 'Yy':
            emp_id = int(input('Enter your employee id: '))
            if emp_id in list_ids:
                print('This employee already exists \n Try again please')
            else:
                emp_name = input('Type your name: ')
                emp_email = input('Type your email: ')
                emp_phone = input('Type your phone: ')
                emp_address = input('Type your address: ')
                emp_salary = input('Type your salary: ')
                emp = (emp_id,emp_name, emp_email, emp_phone, emp_address, emp_salary)
                qry = 'insert into employee values (%s,%s,%s,%s,%s,%s);'
                val = emp
                cur.execute(qry, val)
                con.commit()
                print('Employee added')
                ask = input('Do you want to add more employees? Press Y/y for yes or N/n for no \n')
                if ask not in ('Yy'):
                    break
                return val


#Προβολη στοιχειων υπαλληλου
    def view_emp(self):
        qry='select id from employee;'
        cur.execute(qry)
        c=cur.fetchall()
        for i in c:
            print("Employee id: ", i[0])
        print("Select one of the above ids to view details \n")
        emp_id=input('Enter employee id: ')
        qry='select * from employee where id=%s'
        val=(emp_id,)
        cur.execute(qry,val)
        cemp=cur.fetchall()
        for i in cemp:
            print("Employee name: ", i[1])
            print("Employee email: ", i[2])
            print("Employee phone: ", i[3])
            print("Employee address: ", i[4])
            print("Employee salary: ", i[5])
            print("\n")


# function για την επεξεργασία στοιχείων ενός υπαλλήλου
#Σημείωση: Παρόλο που τρέχει ο κώδικας χωρίς error δεν περνάνε οι αλλαγές στην βάση
    def edit_emp(self):
        ask = 'Y'
        list_ids = check()
        while ask in 'Yy':
            emp_id = int(input('Enter your employee id: '))
            if emp_id not in list_ids:
                print('This employee doesnt exist \n Try again please')
            else:
                emp_name = input('Type your name: ')
                emp_email = input('Type your email: ')
                emp_phone = input('Type your phone: ')
                emp_address = input('Type your address: ')
                emp_salary = input('Type your salary: ')
                emp = (emp_id, emp_name, emp_email, emp_phone, emp_address, emp_salary)
                qry='update employee set name= (%s), email=(%s), phone=(%s), address=(%s), salary=(%s) where id=(%s)'
                val=emp
                cur.execute(qry,val)
                con.commit()
                print(cur.rowcount,'details updated') #Το rowcount μου δειχνει οτι δεν εχει κανει κανενα update
                return val


#Για την προαγωγη υπαλληλου
#Συμβαινει το ιδιο οπως και στο edit
    def promote_emp(self):
        emp_id = int(input("enter employ's id: "))
        qry = "SELECT salary from employee where id = %s"
        cur.execute(qry,(emp_id,))
        con.commit()
        c=cur.fetchone()
        for i in c:
            print("employee salary: ", i[0])
        prom = float(input("enter promotion amount: "))
        cur.execute(qry, (prom,))
        s = cur.fetchone()
        for i in s:
            p = tuple(s[5] + prom)
            qry = "UPDATE employee set salary= salary+ %s where id = %s"
            cur.execute(qry,p)
            cur.commit()
            return p



#Διαγραφή υπαλλήλου απο την βάση
    def delete_emp(self):
        id=int(input("Enter id of employee to delete: "))
        c= str(input("If you agree deleting this employee details press Yy if not press Nn: \n"))
        while c not in 'YyNn':
            print("Please use one of the above")
            c = str(input("If you agree deleting this employee details press Yy if not press Nn: \n"))
            if c in 'Yy':
                query = "DELETE from employee where id = %s"
                cur.execute(query,(id,))
                con.commit()
                print("employee deleted")
                break
            else:
                continue


#Αναζητηση υπαλληλου απο την βαση
    def search_emp(self):
        ask = 'Y'
        list_of_ids = check()
        while ask in 'Yy':
            emp_id = int(input('Enter your employee id: '))
            if emp_id not in list_of_ids:
                print('This employee doesnt exist \n Try again please')
            else:
                qry='select * from employee where id=%s'
                cur.execute(qry,(emp_id,))
                emp_details= cur.fetchall()
                for emp in emp_details:
                    print("ID: ", emp[0])
                    print("Name: ", emp[1])
                    print("Email: ", emp[2])
                    print("Phone: ", emp[3])
                    print("Address: ", emp[4])
                    print("Salary: ", emp[5])
                cont=str(input("Do you wish to continue? If Yes press 'Yy', if not press 'Nn': \n"))
                while cont not in 'YyNn':
                    print("Wrong letter please use one of the above \n")
                    cont = str(input("Do you wish to continue? If Yes press 'Yy', if not press 'Nn': \n"))
                else:
                    if cont in 'Yy':
                        continue
                    else:
                        break






#Μενού με τις διαθέσιμες επιλογές
print("Welcome to employee management system \n")
print("Please choose one of the following options")
print("1 to Add an employee ")
print("2 to Show employee info")
print("3 to Edit employee info")
print("4 to Promote employee")
print("5 to Delete employee")
print("6 to Search employee")
print("7 to exit")
choice = int(input("Choose one of the following options \n "))


def check():
    qry = "select id from employee;"
    cur.execute(qry)
    c = cur.fetchall()
    list_ids = []
    for ids in c:
        list_ids.append(ids[0])
    return list_ids

def menu():

    if choice== 1:
        emp=Employee()
        emp.add_emp()
    elif choice==2:
        emp = Employee()
        emp.view_emp()
    elif choice==3:
        emp=Employee()
        emp.edit_emp()
    elif choice==4:
        emp=Employee()
        emp.promote_emp()
    elif choice==5:
        emp=Employee()
        emp.delete_emp()
    elif choice==6:
        emp=Employee()
        emp.search_emp()
    elif choice==7:
        exit()
    else:
        print("Wrong input. Please try one of the following")
menu()









