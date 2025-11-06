class employee:
    language="python"
    salary=1200000

    def __init__(self,name,language,salary):
        self.name=name
        self.language=language
        self.salary=salary
        # prit("ia ma creating an oobject")
       

    # def getInfo():
    #     print(f"The language is {self.language} and salary is {self.salary}")

a=employee("chandani","javascript",1200000)
print(a.name,a.language,a.salary)
    