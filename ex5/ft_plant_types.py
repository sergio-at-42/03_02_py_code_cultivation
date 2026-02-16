#!/usr/bin/env python3

from typing import Self


class Plant:

    def __init__(self, name: str, height: int = 0, age: int = 0):
        self.name: str = name
        self.starting_age: int = age
        self.age: int = age
        self.starting_height: int = height
        self.height: int = height

    def get_name(self) -> str:
        return (self.name)

    def get_age(self) -> int:
        return (self.age)

    def get_height(self) -> int:
        return (self.height)

    def set_name(self, name: str) -> Self:
        self.name = name
        return (self)

    def set_age(self, days: int) -> int:
        if days > 0:
            self.age = days
            return (0)
        else:
            return (1)

    def set_height(self, height: int) -> int:
        if height > 0:
            self.height = height
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
        print(self.name, ":  ", self.height, sep="", end="")
        print(self.age, " days old", sep="")


class Flower(Plant):

    def __init__(self, name: str, height: int = 0, age: int = 0,
                 color: str = "rouge"):
        super().__init__(name, height, age)
        self.color: str = color

    def get_color(self) -> str:
        return (self.color)

    def set_color(self, color: str) -> Self:
        self.color = color
        return (self)

    def bloom(self) -> Self:
        return (self)


class Tree(Plant):

    def __init__(self, name: str, height: int = 0, age: int = 0,
                 trunk: int = 0, shade: int = 0):
        super().__init__(name, height, age)
        self.trunk: int = trunk
        self.shade: int = shade

    def get_trunk(self) -> int:
        return (self.trunk)

    def set_trunk(self, trunk: int) -> Self:
        self.trunk = trunk
        return (self)

    def produce_shade(self) -> int:
        return (self.shade)


class Vegetable(Plant):

    def __init__(self, name: str, height: int = 0, age: int = 0,
                 harvest: str = "summer", nutrition: int = 0):
        super().__init__(name, height, age)
        self.harvest: str = harvest
        self.nutrition: int = nutrition

    def get_harvest(self) -> str:
        return (self.harvest)

    def get_nutrition(self) -> int:
        return (self.nutrition)

    def set_harvest(self, harvest: str) -> Self:
        self.harvest = harvest
        return (self)

    def set_nutrition(self, nutrition: int) -> Self:
        self.nutrition = nutrition
        return (self)


def ft_creat_plant(stream: list) -> Plant:
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


def ft_plant_types():
    streamline = [["flower", "Rose", 25, 15, "red"],
                  ["flower", "Tulipe", 30, 12, "yellow"],
                  ["tree", "Oak", 500, 1825, 50, 78],
                  ["tree", "Chestnut", 650, 3650, 64, 42],
                  ["vegetable", "Tomato", 80, 90, "summer", 15],
                  ["vegetable", "Chili pepper", 64, 42, "fall", 20]]
    plants: list[Plant | Flower | Tree | Vegetable] = []
    for stream in streamline:
        plants.append(ft_creat_plant(stream))
    print("=== Garden Plant Types ===")
    print("")
    for plant in plants:
        print(f"{plant.name} ({type(plant).__name__}):", end=" ")
        print(f"{plant.get_height()}cm, {plant.get_age()} days,", end=" ")
        match type(plant).__name__:
            case "Flower":
                print(f"{plant.get_color()} color")
                print(f"{plant.name} is blooming beautifully!")
            case "Tree":
                print(f"{plant.get_trunk()}cm diameter")
                print(f"{plant.name} provides {plant.produce_shade()} square meters of shade")
            case "Vegetable":
                print(f"{plant.get_harvest()} harvest")
                print(f"{plant.name} contains {plant.get_nutrition()} Kcal per 100g")
        print("")

if __name__ == "__main__":
    ft_plant_types()
