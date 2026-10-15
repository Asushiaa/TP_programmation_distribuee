
class Cat:
    def __init__(self, cat_id, name, breed, age, status="available"):
        self.id = cat_id
        self.name = name
        self.breed = breed
        self.age = age
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "breed": self.breed,
            "age": self.age,
            "status": self.status
        }
