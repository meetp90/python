class Employee():
    def __init__(self,name) -> None:
        self.name = name
    def __str__(self) -> str:
        return f"{self.name}"
    
class Tester(Employee):
    def __init__(self,name):
        super().__init__(name)

class Developer(Employee):
    def __init__(self,name):
        super().__init__(name)

class Manager(Employee):
    def __init__(self,name):
        super().__init__(name)
        self.manage = []

    def add(self,name):
        self.manage.append(name)
    
    def remove(self,name):
        self.manage.remove(name)

    def display(self):
        [print(i) for i in self.manage]
    
def main():
    e1 = Tester("meet")
    e2 = Developer("dev")
    e3 = Manager("man")
    e3.add(e1)
    e3.add(e2)
    e3.display()
    e3.remove(e2)
    e3.display()

main()