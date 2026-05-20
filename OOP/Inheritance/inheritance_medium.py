class Employee:
    def __init__(self, name, salary):
        self.name= name
        self.salary= salary

    def show_details(self):
        print("Name= ", self.name)
        print("Salary= ", self.salary)

class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department= department

    def show_details(self):
        super().show_details()
        print("Department= ", self.department)

spk= Manager("Spandan",80000,"Risk & Advisory")
spk.show_details()