#!/usr/bin/python3
"""FileStorage class"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Represent the storage engine.

    Attributes:
        __file_path(str): The file name to save objects to.
        __objects(dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(save):
        """Return the dictionary __objects."""
        return FileStorage.__objects
    
    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        obj_clsname = obj.__class__.__name__
        FileStorage.__objects[f"{obj_clsname}.{obj.id}"] = obj

    def save(slef):
        """Serialize __objects to the JSON file (path: __file_path)"""
        dic = FileStorage.__objects
        objdict = {obj: dic[obj].to_dict() for obj in dic.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file to __objects if the file exists"""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for obj in objdict.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return