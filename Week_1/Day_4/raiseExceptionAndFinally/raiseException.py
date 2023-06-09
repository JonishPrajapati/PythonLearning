# class ManageDatatype(Exception):
#     def __init__(self,msg):
#         self.msg = msg
#     def print_exception(self):
#         print("user defined exception:", self.msg)

# try:
#     raise ManageDatatype('Human error')
# except ManageDatatype as e:
#        e.print_exception()


# class AdultException(Exception):
#       pass
# #      def __init__(self,message):
# #           self.msg = message
# #      def print_message(self):
# #           print("Custom Exception Message:", self.msg)

# # try:
# #      raise AdultException("Adult Error")
# # except AdultException as a:
# #      a.print_message()


# class Person():
#      def __init__(self,name,age):
#           self.name = name
#           self.age = age
#      def get_minor_age(self):
#                if self.age > 18:
#                     print("he is an adult")
#                else:
#                     raise AdultException()
       
#      def display_person(self):
#           try:
#                print(p.get_minor_age())
#           except AdultException:
#                print("person is an adult")
#           finally:
#                print(f"{self.name}:{self.age}")
     
# p = Person("jonish",3)
# p.display_person()

# p1 = Person("jony",29)
# p1.display_person()

# for making exception just make subclass of Exception
class AdultException(Exception):
    pass


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_minor_age(self):
        if int(self.age) >= 18:
            raise AdultException("Person is an adult.")
        else:
            return self.age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Example usage
person1 = Person("John Doe", 25)
person2 = Person("Jane Smith", 16)
try:
    age = person1.get_minor_age()
    person1.display_person()
    print("Minor age:", age)
except AdultException as e:
    print("Exception:", e)

print()

try:
    age = person2.get_minor_age()
    person2.display_person()
    print("Minor age:", age)
except AdultException as e:
    print("Exception:", e)