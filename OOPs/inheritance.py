class employee:
    company="ITC"
    name="Default name"

    def show(self):
        print(f"The name of the employee is {self.name} and company is {self.company}")

class coder:
    language="python"

    def language(self):
        print(f"your language is {self.language}")

class programmer(employee,coder):
    company="ITC infotech"

    def showlanguage(self):
        print(f'The name is {self.company} and language is {self.language}')

a=employee()
b=programmer()

b.show()
b.language()
b.showlanguage()