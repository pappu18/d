class Student:
  def __init__(self, Name, Rollno):
    self.Name = Name
    self.Rollno = Rollno
  def setAge(self, age):
    self.age = age
  def setmarks(self, marks):
    self.marks = marks
  def display(self):
    print("Student Details")
    print("---------------")
    print("Name : ", self.Name)
    print("Roll Number :", self.Rollno)
    print("Age : ", self.age)
    print("Marks : ", self.marks)
s = Student("Ash", 123)
s.setAge(18)
s.setmarks(100)
s.display()
