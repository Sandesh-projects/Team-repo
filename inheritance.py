class Animal():
    def __init__(self):
        self.number_of_eye = 2

    def breathe(self):
        print("Inhale, Exhale")


class Fish(Animal):

    def __init__(self):# it inherit all the property of the Animal class by the super keyword and the intialiser
        super().__init__()

    # addint the content to the parent class using the child class
    def breathe(self):
        super().breathe()
        print("Updated\nBreathing is done underwater")
    
    def swim(self):
        print("It is a swimming Animal")
#inheritance function calling
        
Fish_1 = Fish()# creating object
# calling the super class with the other class object/before update/after update the content insider the super class function change
Fish_1.breathe()

Fish_1.swim()#calling inside the function
print(Fish_1.number_of_eye)#calling the variable of super class







# normal function calling
Fish = Fish()
Fish.swim()

Animal = Animal()
Animal.breathe()# here the calling is done direct to the main function content breathe so the content is not update over here 
