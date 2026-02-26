#!/usr/bin/env python3

from typing import Self


class Plant:

    def __init__(self, name: str, height: int = 0, age: int = 0):
        self._name: str = ""
        self._age: int = 0
        self._height: int = 0
        self.set_name(name)
        self.set_age(age)
        self.set_height(height)

    def get_name(self) -> str:
        return (self._name)

    def get_age(self) -> int:
        return (self._age)

    def get_height(self) -> int:
        return (self._height)

    def set_name(self, name: str) -> Self:
        self._name = name
        return (self)

    def set_age(self, days: int) -> int:
        if days > 0:
            self._age = days
            return (0)
        else:
            return (1)

    def set_height(self, height: int) -> int:
        if height > 0:
            self._height = height
            return (0)
        else:
            return (1)

    def error_msg_age(self, days: int) -> str:
        msg = f"Invalid operation attempted: age {days} days [REJECTED]\n"
        msg += "Security: Negative age rejected"
        return (msg)

    def error_msg_height(self, height: int) -> str:
        msg = f"Invalid operation attempted: height {height}cm [REJECTED]\n"
        msg += "Security: Negative height rejected"
        return (msg)

    def get_info(self):
        print(self.get_name(), ":  ", self.get_height(), sep="", end="")
        print(self.get_age(), " days old", sep="")


class Flower(Plant):

    def __init__(self, name: str, height: int = 0, age: int = 0,
                 color: str = "rouge"):
        super().__init__(name, height, age)
        self._color: str = color

    def get_color(self) -> str:
        return (self._color)

    def set_color(self, color: str) -> Self:
        self._color = color
        return (self)

    def bloom(self) -> Self:
        return (self)


class Tree(Plant):

    def __init__(self, name: str, height: int = 0, age: int = 0,
                 trunk: int = 0, shade: int = 0):
        super().__init__(name, height, age)
        self._trunk: int = trunk
        self._shade: int = shade
        self.set_trunk(trunk)
        self.set_shade(shade)

    def get_trunk(self) -> int:
        return (self._trunk)

    def get_shade(self) -> int:
        return (self._shade)

    def set_trunk(self, trunk: int) -> Self:
        self._trunk = trunk
        return (self)

    def set_shade(self, shade: int) -> Self:
        self._shade = shade
        return (self)


class Vegetable(Plant):

    def __init__(self, name: str, height: int = 0, age: int = 0,
                 harvest: str = "summer", nutrition: int = 0):
        super().__init__(name, height, age)
        self._harvest: str = harvest
        self._nutrition: int = nutrition

    def get_harvest(self) -> str:
        return (self._harvest)

    def get_nutrition(self) -> int:
        return (self._nutrition)

    def set_harvest(self, harvest: str) -> Self:
        self._harvest = harvest
        return (self)

    def set_nutrition(self, nutrition: int) -> Self:
        self._nutrition = nutrition
        return (self)


def ft_creat_plant(stream: list) -> Plant:
    plant: Plant
    match stream[0]:
        case "flower":
            plant = Flower(stream[1], stream[2], stream[3], stream[4])
        case "tree":
            plant = Tree(stream[1], stream[2], stream[3],
                         stream[4], stream[5])
        case "vegetable":
            plant = Vegetable(stream[1], stream[2], stream[3],
                              stream[4], stream[5])
        case _:
            plant = Plant(stream[1], stream[2], stream[3])
    return (plant)


def ft_plant_types() -> None:
    streamline = [["flower", "Rose", 25, 15, "red"],
                  ["flower", "Tulipe", 30, 12, "yellow"],
                  ["tree", "Oak", 500, 1825, 50, 78],
                  ["tree", "Chestnut", 650, 3650, 64, 42],
                  ["vegetable", "Tomato", 80, 90, "summer", 15],
                  ["vegetable", "Chili pepper", 64, 42, "fall", 20]]
    plants: list = []
    for stream in streamline:
        plants.append(ft_creat_plant(stream))
    print("=== Garden Plant Types ===")
    print("")
    for p in plants:
        print(f"{p.get_name()} ({type(p).__name__}):", end=" ")
        print(f"{p.get_height()}cm, {p.get_age()} days,", end=" ")
        match type(p).__name__:
            case "Flower":
                print(f"{p.get_color()} color")
                print(f"{p.get_name()} is blooming beautifully!")
            case "Tree":
                print(f"{p.get_trunk()}cm diameter")
                print(f"{p.get_name()} provides {p.get_shade()}", end=" ")
                print(" square meters of shade")
            case "Vegetable":
                print(f"{p.get_harvest()} harvest")
                print(f"{p.get_name()}", end=" ")
                print(f"contains {p.get_nutrition()} Kcal per 100g")
        print("")


if __name__ == "__main__":
    ft_plant_types()
