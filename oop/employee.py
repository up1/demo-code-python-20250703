class Employee:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.start_working_date = ""

    def leave(self):
        print("Employee has left the company.")


e = Employee()
e.id = 1
e.name = "Somkiat"
e.start_working_date = "2022-01-01"
print(e.id)
print(e.name)
print(e.start_working_date)
e.leave()