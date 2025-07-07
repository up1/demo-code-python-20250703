class Employee:
    def __init__(self, employee_type="permanent"):
        self.employee_type = employee_type

    def compute_pay(self, hours_worked, hourly_rate):
        if self.employee_type == "permanent":
            return self.compute_permanent_pay(hours_worked, hourly_rate)
        elif self.employee_type == "contract":
            return self.compute_contract_pay(hours_worked, hourly_rate)
        else:
            raise ValueError("Unknown employee type")

    def compute_permanent_pay(self, hours_worked, hourly_rate):
        return hours_worked * hourly_rate

    def compute_contract_pay(self, hours_worked, hourly_rate):
        return hours_worked * hourly_rate * 1.2
    
# Example usage:
if __name__ == "__main__":
    emp1 = Employee("permanent")
    print(emp1.compute_pay(40, 20))  # Output: 800

    emp2 = Employee("contract")
    print(emp2.compute_pay(40, 20))  # Output: 960