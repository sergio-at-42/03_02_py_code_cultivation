#!/usr/bin/env python3

from typing import Self


class GardenManager:

    def __init__(self, name: str) -> None:
        self.name: str = ""
        self.plants: list[Plant | FloweringPlant | PrizeFlower | Tree | Vegetable] = []
        self.set_name(name)

    def get_name(self) -> str:
        return (self.name)

    def set_name(self, name: str) -> Self:
        self.name = name
        return (self)


#def garden

class Plant:

    def __init__(self, name: str, height: int = 0, age: int = 0) -> None:
        self.name: str = ""
        self.age: int = 0
        self.height: int = 0
        self.set_name(name)
        self.set_age(age)
        self.set_height(height)

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


class FloweringPlant(Plant):

    def __init__(self, name: str, height: int = 0, age: int = 0,
                 color: str = "no") -> None:
        super().__init__(name, height, age)
        self.color: str = ""
        self.set_color(color)

    def get_color(self) -> str:
        return (self.color)

    def set_color(self, color: str) -> Self:
        self.color = color
        return (self)

    def bloom(self) -> Self:
        return (self)


class PrizeFlower(FloweringPlant):

    def __init__(self, name: str, height: int = 0, age: int = 0, 
                 color: str = "", prize: int = 0) -> None:
        super().__init__(name, height, age, color)
        self.prize: int = 0
        self.set_prize(prize)

    def get_prize(self) -> int:
        return (self.prize)

    def set_prize(self, prize: int) -> Self:
        self.prize = prize
        return (self)


class Tree(Plant):

    def __init__(self, name: str, height: int = 0, age: int = 0,
                 trunk: int = 0, shade: int = 0) -> None:
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
                 harvest: str = "summer", nutrition: int = 0) -> None:
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


def ft_creat_garden(stream: list) -> GardenManager:
    
    garden = GardenManager(stream[0])
    return (garden)


def ft_creat_plant(stream: list) -> Plant:
    match stream[1]:
        case "flower":
            plant = FloweringPlant(stream[2], stream[3], stream[4], stream[5])
        case "prizeflower":
            plant = PrizeFlower(stream[2], stream[3], stream[4], stream[5], stream[6])
        case "tree":
            plant = Tree(stream[2], stream[3], stream[4],
                         stream[5], stream[6])
        case "vegetable":
            plant = Vegetable(stream[2], stream[3], stream[4],
                              stream[5], stream[6])
        case _:
            plant = Plant(stream[2], stream[3], stream[4])
    return (plant)


def ft_garden_analytics():
    streamline = [["Alice", "flower", "Rose", 25, 15, "red"],
                  ["Alice", "prizeflower", "Sunflower", 50, 12, "yellow", 10],
                  ["Alice", "tree", "Oak", 500, 1825, 50, 78],
                  ["Tatiana", "flower", "Tulipe", 42, 16, "blue"],
                  ["Bob", "tree", "Chestnut", 650, 3650, 64, 42],
                  ["Bob", "vegetable", "Tomato", 80, 90, "summer", 15],
                  ["Bob", "vegetable", "Chili pepper", 64, 42, "fall", 20]]
    gardens: list [GardenManager] = []
    plants: list[Plant | FloweringPlant | Tree | Vegetable] = []
    for stream in streamline:
        garden = next((g for g in gardens if g.get_name() == stream[0]), None)
        if garden == None:
            garden = GardenManager(stream[0])
            gardens.append(garden)
        garden.plants.append(ft_creat_plant(stream))

    print("=== Garden Management System Demo ===")
    print("")
    for g in gardens:
        print(f"=== {g.name}'s Garden Report ===")
    # for p in plants:
    #     print(f"{p.name} ({type(p).__name__}):", end=" ")
    #     print(f"{p.get_height()}cm, {p.get_age()} days,", end=" ")
    #     match type(p).__name__:
    #         case "Flower":
    #             print(f"{p.get_color()} color")
    #             print(f"{p.name} is blooming beautifully!")
    #         case "Tree":
    #             print(f"{p.get_trunk()}cm diameter")
    #             print(f"{p.name} provides {p.produce_shade()}", end=" ")
    #             print(" square meters of shade")
    #         case "Vegetable":
    #             print(f"{p.get_harvest()} harvest")
    #             print(f"{p.name} contains {p.get_nutrition()} Kcal per 100g")
    #     print("")


if __name__ == "__main__":
    ft_garden_analytics()
