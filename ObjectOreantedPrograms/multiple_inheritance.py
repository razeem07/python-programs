class Person:

    def __init__(self,name,age):

        self.name=name
        self.age=age

    def dispaly_person_info(self):

        print(self.name,self.age)

class Employee:

    def __init__(self,eid,salary):

        self.eid=eid
        self.sarary=salary

    def dispaly_employee_info(self):

        print(self.eid,self.sarary)

class Manager(Person,Employee):

    def __init__(self,name,age,eid,salary,department):

        Person.__init__(self,name,age)
        Employee.__init__(self,eid,salary)
        self.department=department

    def dispaly_manager_info(self):

        self.dispaly_person_info()

        self.dispaly_employee_info()

        print(self.department)

manager_instance1=Manager("vaishnav", 29, "e2019", 100000, "Developer" )
manager_instance1.dispaly_manager_info()



# manager_instance1=Manager("Rob",29,991,79000,"HR")
# manager_instance1.display_person_info()
# manager_instance1.display_employee_info()



