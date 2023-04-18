class Human:
  def __init__(self,name,age):
    self.name = name
    self.age = age
  def get_name(self):
    return self.name
  def get_age(self):
    return self.age
    
class Student(Human):
  def __init__(self,name,grade):
    self.name = name
    self.grade = grade
  def get_grade(self):
    return self.grade
    
class Students:
  def __init__(self,students):
    self.students = students
    
  def get_student(self,pos):
    student = self.students[pos]
    return student
    
  def get_names(self):
    list = []
    for x in self.students:
      list.append(x.get_name())
    return list
  def get_grades(self):
    list = []
    for x in self.students:
      list.append(x.get_grade())
    return list
    
class School:
  def __init__(self,classes):
    self.classes = classes
    
  def all_names(self):
    temp = []
    for f in self.classes:
      temp.append(f.get_names())
    for x in temp:
      for y in x:
        print(y, end = ", ")
      print("\n")
  def all_grades(self):
    temp = []
    for f in self.classes:
      temp.append(f.get_grades())
    for x in temp:
      for y in x:
        print(y, end = ", ")
      print("\n")
          
## New humans are declared   
Antonio = Human("Antonio",18)
Lillian  = Human("Lillian",17)
Roberto  = Human("Roberto ",17)
Janice   = Human("Janice ",18)
fred = Human("fred",16)
bob  = Human("bob",15)
mat  = Human("Roberto ",17)
jace   = Human("jace ",18)

## New students are declared
student1 = Student(Antonio.get_name(),12)
student2 = Student(Lillian.get_name(),12)
student3 = Student(Roberto.get_name(),11)
student4 = Student(Janice.get_name(),11)
student5 = Student(fred.get_name(),12)
student6 = Student(bob.get_name(),12)
student7 = Student(mat.get_name(),11)
student8 = Student(jace.get_name(),11)

## New classes of students are declaed
class12 = Students([student1,student2,student5,student6])
class11 = Students([student3,student4,student7,student8])

test_school = School([class12,class11])
test_school.all_names()
test_school.all_grades()


