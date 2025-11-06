class Employee:
    language="python"
    salary=1200000

    def getInfo(self):
         print(f"The language is {self.language} and salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("good morning")

a=Employee()
a.getInfo()
a.greet()