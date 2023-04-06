from functools import partial

MANAGEMENT_GROUP_DEFAULT_VALUE = 1

class ObjectManager():

    def __init__(
        self,
        name:str,
        management_group=MANAGEMENT_GROUP_DEFAULT_VALUE,
    ):
        self.managed_class_name= name
        self.objects = []
        self.getter_from_id = {}
        self.getter_from_no = {}
        self.getter_from_name = {}
        self.group = management_group
    
    def init_manager(
        self,
        new_function,
        *args,
        **kwargs,
    ):
        def init_wrapper(*args,**kwargs):
            
            new_object = new_function(*args,**kwargs)
            self.objects.append(new_object)
        
        return init_wrapper

def managed_class(cls,management_group=MANAGEMENT_GROUP_DEFAULT_VALUE):
    cls.manager = ObjectManager(name=cls.__name__,management_group=management_group)
    cls.is_managed = True
    cls.__init__ = cls.manager.init_manager(cls.__init__)
    
    return cls

def managed_class_group(management_group=MANAGEMENT_GROUP_DEFAULT_VALUE):
    return partial(managed_class,management_group=management_group)