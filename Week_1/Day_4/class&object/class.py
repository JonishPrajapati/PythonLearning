class Employee:
  def __init__(self,id,name):
    self.id = id
    self.name = name
   
  def showDetails(self):
   print(f"ID: {emp.id}\nName: {emp.name}.")

emp = Employee(1,"jonish")
emp.showDetails()
del emp
try:
  print(emp.id)
except NameError as e:
  print("Name error")




