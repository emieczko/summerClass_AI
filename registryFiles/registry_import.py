import registryFiles.registry as registry

student1 = registry.student("bob",9,"3","177 test street")
student1.studentFunc()

s1register = registry.register(student1.name, ["art","music","history","math 1","math 2","writing"])
s1register.func()