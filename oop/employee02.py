class Employee:
    def compute_pay(self, hours_worked, hourly_rate):
        pass

class PermanentEmployee(Employee):
    def compute_pay(self, hours_worked, hourly_rate):
        return hours_worked * hourly_rate

class ContractEmployee(Employee):
    def compute_pay(self, hours_worked, hourly_rate):
        return hours_worked * hourly_rate * 1.2
    
# Example usage:
def call(employee: Employee):
    return employee.compute_pay(40, 20)

if __name__ == "__main__":
    emp1 = PermanentEmployee()
    print(call(emp1))  # Output: 800

    emp2 = ContractEmployee()
    print(call(emp2))  # Output: 960