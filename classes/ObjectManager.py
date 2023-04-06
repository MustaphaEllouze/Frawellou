class ObjectManager():

    def __init__(
        self,
        name:str,
    ):
        self.managed_class_name= name
        self.objects = []
        self.getter_from_id = {}
        self.getter_from_no = {}
        self.getter_from_name = {}
    
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

def managed_class(cls):
    cls.manager = ObjectManager(name=cls.__name__)
    cls.is_managed = True
    cls.__init__ = cls.manager.init_manager(cls.__init__)
    
    return cls