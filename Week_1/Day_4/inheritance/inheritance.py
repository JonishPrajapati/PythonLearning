# class Animal():
#     def __init__(self,name,color):
#         self.name = name
#         self.color = color

#     def displayDetails(self):
#         print(f"name: {self.name}\n color:{self.color}")


# class Dog(Animal):
#     def __init__(self, name, color):
#        super().__init__(name,color)

# a = Animal("german sheperd", "black")
# d = Dog("corgies","brown")
# d.displayDetails()


        


class Animal:
    def __init__(self, habitat):
        self.habitat = habitat

    def print_habitat(self):
        print(self.habitat)

    def sound(self):
        print("Some Animal Sound")


class Dog(Animal):
    def __init__(self):
        super().__init__("Kennel")

    def sound(self):
        print("Woof woof!")


x = Dog()
x.print_habitat()
x.sound()