import dis
 


def hello():
   print("Hello, World!")
 
dis.dis(hello)
 
dis.show_code(hello)
 
print(hello.__code__)
 
print(hello.__code__.co_code)
 
print(list(hello.__code__.co_code))
