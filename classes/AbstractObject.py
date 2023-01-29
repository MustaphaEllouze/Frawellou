from abc import (
    ABC,
    abstractmethod,
)

class AbstractObject(ABC):
    
    # def init_class_attributes():
    #     object_from_id =   {}
    #     object_from_no =   {}
    #     object_from_name = {}
    #     return (object_from_id,
    #             object_from_no,
    #             object_from_name,
    #             )

    @abstractmethod
    def do_something():
        pass

