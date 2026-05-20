class Employee:
    def __init__(self, name):
        self.name= name

    def employee_info(self):
        print("Employee Name= ", self.name)

class Developer(Employee):
    def __init__(self,name, programming_language):
        super().__init__(name)
        self.programming_language= programming_language

    def developer_info(self):
        print("Developer name= ", self.name)
        print("Programming language= ", self.programming_language)

class SeniorDeveloper(Developer):
    def __init__(self,name,programming_language,experience):
        super().__init__(name,programming_language)
        self.experience= experience

    def senior_developer_info(self):
        self.developer_info()
        print("Experience= ", self.experience)


developer= SeniorDeveloper("Spandan","Python",5)
developer.senior_developer_info()