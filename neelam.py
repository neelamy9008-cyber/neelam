#student detail

print("------student Details-------")
class Student:
    #constructor
    def __init__(self,name,age,rollno,result):
     self.name=name 
     self.age=age
     self.rollno=rollno
     self.result=result
    #method
    def display(self):
        print("name=",self.name)
        print("age=",self.age)
        print("roll no=",self.rollno)
        print("result=",self.result)
#objects
s1=Student("neelam",18,25,"Pass")
s1.display()

print("-------employee Details--------")
#employee deatils
class employee:
    #constructor
    def __init__(self,name,salary,years):
     self.name=name 
     self.salary=salary
     self.years=years
     
    #method
    def display(self):
        print("name=",self.name)
        print("Salary of the employee",self.salary)
        print("years of working=",self.years)
       
#objects
s1=employee("neelam",25000,5)
s1.display()

#faculty deatails
print("-------Faculty Details--------")
#employee deatils
class faculty:
    #constructor
    def __init__(self,name,salary,years,post):
     self.name=name 
     self.salary=salary
     self.years=years
     self.post=post
    #method
    def display(self):
        print("name=",self.name)
        print("Salary of the faculty",self.salary)
        print("years of teaching=",self.years)
        print("post of the faculty=",self.post)
#objects
s1=employee("neelam",25000,5,"junior professor")
s1.display()





