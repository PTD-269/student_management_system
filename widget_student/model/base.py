from abc import ABC, abstractmethod

class AbstractModel(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def insert(self, id):
        pass

    @abstractmethod
    def delete(self, id):
        pass
    
    @abstractmethod
    def edit(self, id):
        pass
    
    @abstractmethod
    def sort_name(self):
        pass
    
    @abstractmethod
    def sort_average_point(self):
        pass
    
    @abstractmethod
    def find_highest_scrore(self):
        pass

    @classmethod
    def convert_objects_to_dict(cls, entity, objs):
        cols_name = entity.get_columns_name()
        # objs_as_dict: limit key with multi values
        objs_as_dict = {col_name: [] for col_name in cols_name}
            

        # objs_as_dicts: list with multi dicts object attribute values
        objs_to_dicts = [obj.__dict__ for obj in objs] # [{"name":"Dat", "age":18}, {"name":"Nhan", "age":18}, {"name":"Luan", "age":18}]
        objs_to_dicts_without_sa_instance_state = [{k: v for k, v in obj.items() if k != '_sa_instance_state'} for obj in objs_to_dicts]
        # Each obj_as_dict added to 
        for dic in objs_to_dicts_without_sa_instance_state:
            for key,value in dic.items():
                objs_as_dict[key].append(value)

        return objs_as_dict
    
