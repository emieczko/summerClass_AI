#registry class
class register:
    def __init__(self, name, courses):
        self.Sname = name
        self.courses = courses
    
    def func(self):
        iter = 0
        print(self.Sname, "takes ", end='')
        #really ugly way to make the output look pretty
        for c in self.courses:
            iter += 1
            if iter == 1:
                print(c + ", ", end='')
            elif iter < len(self.courses):
                print(c + ", ", end='')
            else:
                print("and", c)
        print("")
#student class
class student:
    def __init__(self, name, age, grade, address):
        self.name = name
        self.age = age
        self.grade = grade
        self.address = address
    
    def studentFunc(self):
        print(self.name, "is", self.age, "years old, in grade", self.grade + ", and lives on",self.address)

student1 = student("Bob",10,"4","10 Example Road") #attributes for student class
student1.studentFunc()
s1Register = register(student1.name, ["math", "english", "science", "history", "art", "music"]) #attributes for registry class
s1Register.func()