class EmployeeInfo:
    def __init__(self, name, salary, transport, food):
        self.name = name
        self.salary = salary
        self.transport = transport
        self.food = food
        
    def expense(self):
        return self.salary + self.transport + self.food
    
    def __str__(self):
        print("=" * 40)
        print("       EMPLOYEE PAYSLIP")
        print("=" * 40)
        print(f"Employee: {self.name}")
        print(f"Basic Salary: {self.salary} ETB")
        print(f"Transport Allowance: {self.transport} ETB")
        print(f"Food Allowance: {self.food} ETB")
        print("-" * 40)
        print(f"Gross Salary: {self.expense()} ETB")
        print("=" * 40)