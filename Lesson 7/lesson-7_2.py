from abc import ABC, abstractmethod


class Room:
    cloth_list = []

    def add_clothes(self, clothes):
        self.cloth_list.append(clothes)

    def summ(self):
        return sum(item.material for item in self.cloth_list)
    # def create_clothes(self, cls_clothes, *args, **kwargs):
    #     self.cloth_list.append(cls_clothes(*args, **kwargs))


class Clothes(ABC):  # абстрактный класс т.е., класс-потомок наследует интерфейс родителя.
    def __init__(self, val):
        self.val = val

    @abstractmethod  # декоратор абстактного метода
    def material(self):
        pass


class Costume(Clothes):
    @property  # позволяет работать с методом как с атрибутом
    def material(self):
        return round(2 * self.val + 0.3)


class Coat(Clothes):
    @property
    def material(self):
        return round(self.val / 6.5 + 0.5)


wardrobe = Room()
ct = Coat(48)
cs = Costume(165)
wardrobe.add_clothes(ct)
wardrobe.add_clothes(cs)
print(ct.material, cs.material, wardrobe.summ())
# wardrobe.create_clothes(Coat,48)
# wardrobe.create_clothes(Coat,52)
# wardrobe.create_clothes(Costume,175)
# wardrobe.create_clothes(Costume,165)
# print (wardrobe.summ())
# print([item.summ for item in wardrobe.cloth_list])
