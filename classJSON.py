import json
from datetime import datetime

class JSONSerializer:
    def to_json(self):
        data = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                data[key] = value.isoformat()
            else:
                data[key] = value
        return json.dumps(data, ensure_ascii=False, indent=2)
    
    @classmethod
    def from_json(cls, json_string):
        data = json.loads(json_string)
        obj = cls.__new__(cls)
        obj.__dict__.update(data)
        return obj
    
class Person(JSONSerializer):
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        self.created_at = datetime.now()

person = Person("Иван Дурачок", 27, "ivan@durak.ru")

json_string = person.to_json()
print(json_string)