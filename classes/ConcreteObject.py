from ObjectManager import(
    ObjectManager,
)

class ConcreteObject():

    manager = ObjectManager(name='ConcreteObject')

    @manager.init_manager
    def __new__(cls,*args,**kwargs):
        return super().__new__(cls)
    
    def __init__(self,value):
        self.value = value
    
    def do_something():
        pass
    

ConcreteObject(5)
ConcreteObject(10)

print(ConcreteObject.manager.__dict__)