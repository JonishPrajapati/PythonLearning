# class Teacher():
#     def skills(self):
#         print("I am a teacher.")

# class Student():
#     def skills(self):
#         print("I am a Student,")

# class Youtuber(Student,Teacher):
#     def skills(self):
      
#         print("I am a youtuber")
#         Teacher.skills(self)
#         Student.skills(self)
# y = Youtuber()
# y.skills()

class Teacher:
    def teachers_action(self):
        print("I can teach")


class Engineer:
    def Engineers_action(self):
        print("I can code")


class Youtuber:
    def youtubers_action(self):
        
        print("I can code and teach")


class Person(Teacher, Engineer, Youtuber):
    def person_action(self):
         Youtuber.youtubers_action(self)


coder = Person()
coder.teachers_action()
coder.Engineers_action()
coder.person_action()