
from entity.cat import Cat


class CatService:
    def __init__(self):
        
        self.cats = [
            Cat(1, "Milo", "Européen", 2),
            Cat(2, "Luna", "Siamois", 4, "adopted"),
            Cat(3, "Minouche", "Européen", 3),
            Cat(4, "Rika", "Chartreux", 5),
            Cat(5, "Kevninouche", "Inconnu", 1),
        ]



    def get_all_cats(self):
        return [cat.to_dict() for cat in self.cats]

    def get_cat_by_id(self, cat_id):
        for cat in self.cats:
            if cat.id == cat_id:
                return cat.to_dict()

        return None
