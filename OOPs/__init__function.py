class employee:
    language="python"
    salary=1200000

    def __init__(self):
        print("I am creating an object")

    # def getInfo():
    #     print(f"The language is {self.language} and salary is {self.salary}")

a=employee()
a.name="chandani"
print(a.name,a.salary)