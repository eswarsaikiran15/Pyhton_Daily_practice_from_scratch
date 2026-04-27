class student:
    def __init__(self,name,marks):
        self.__name=name  # private variable
        self.__marks=marks #private variable

        """
Python allows you to make variables “private” using name mangling (__variable).
But once you hide them, you still need a safe way to:

read the value → getter
update the value → setter
        """

    #getter for name
    def get_name(self):
        return self.__name

    #getter for age
    def get_marks(self):
        return self.__marks

    #setter for age
    def set_marks(self,marks):
        if 0<=marks<=100:
            self.__marks=marks
        else:
            print("marks out of range")


#usage
s1=student("James",100)
print("name",s1.get_name())
print("marks",s1.get_marks())
s1.set_marks(20) #valid update
print("updated marks",s1.get_marks())
s1.set_marks(30) #invalid update