from ObjectManager import managed_class,managed_class_group

@managed_class_group(2)
class ConcreteObject():
    
    def __init__(self,value):
        self.value = value
        return self
    
    def do_something():
        pass
   

ConcreteObject(5)
ConcreteObject(10)

print(ConcreteObject.manager.__dict__)