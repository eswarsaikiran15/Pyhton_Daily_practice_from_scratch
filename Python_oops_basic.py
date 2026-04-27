# pure basics


class Student:
    name="kiran"
    id=1

s1=Student()# object created
s2=Student() # 2nd object created
print(s1.name)
print(s1.id)

s2.name="ravi"
print("after updating 2nd object=",s2.name)
s2.id=2
print("after updating 2nd object id=",s2.id)