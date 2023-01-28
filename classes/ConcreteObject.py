from AbstractObject import (
    AbstractObject,
)

class ConcreteObject(AbstractObject):

    CO_from_id,CO_from_no,CO_from_name = AbstractObject.init_class_attributes()

    def __init__(self,value) -> None:
        super().__init__()
        self.value = value
    
    def do_something():
        pass
    

ConcreteObject(5)