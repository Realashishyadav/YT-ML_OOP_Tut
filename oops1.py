# Initiate a class
class employee:
    # special method/magic method/dunder method-constructor
    def __init__(self):
        print('started executing attributes/data')
        self.id=123
        self.salary=50000
        self.designation="SDE"
        print('attributes/data have been initiated')

    def travel(self,destination):
        print('This travel method was called manually')
        print(f"Employee is now travelling to {destination}")



# create an object/instance of class

sam=employee()

# printing a attributes
#print(sam.salary)

#print(sam.id)


# calling a method
#sam.travel('Kerala')

print(type(sam))
