#!/usr/bin/env python3

from typing import Self


class Garden:

    def __init__(self, gardener: str) -> None:
        self._gardener: str = ""
        self.plants: list[Plant] = []
        self.types_plants: dict[str, int] = {}
        self.set_gardener(gardener)

    def get_gardener(self) -> str:
        return (self._gardener)

    def set_gardener(self, gardener: str) -> Self:
        self._gardener = gardener
        return (self)

    def get_total_grow(self) -> int:
        total_grow: int = 0
        for p in self.plants:
            total_grow += p.get_grow()
        return (total_grow)

    def get_types_plants(self) -> dict[str, int]:
        for p in self.plants:
            self.types_plants.setdefault(type(p).__name__, 0)
            self.types_plants[type(p).__name__] += 1
        return (self.types_plants)

    def get_score(self) -> int:
        score = sum(p.get_height() for p in self.plants)
        return (score)


class Plant:

    def __init__(self, gardener: str, name: str,
                 height: int = 0, age: int = 0) -> None:
        self._gardener: str = ""
        self._name: str = ""
        self._age: int = 0
        self._height: int = 0
        self._grow: int = 0
        self.set_gardener(gardener)
        self.set_name(name)
        self.set_age(age)
        self.set_height(height)

    def get_gardener(self) -> str:
        return (self._gardener)

    def set_gardener(self, gardener: str) -> Self:
        self._gardener = gardener
        return (self)

    def get_name(self) -> str:
        return (self._name)

    def get_age(self) -> int:
        return (self._age)

    def get_height(self) -> int:
        return (self._height)

    def get_grow(self) -> int:
        return (self._grow)

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

    def set_grow(self, grow: int) -> Self:
        self._grow = grow
        return (self)

    @staticmethod
    def error_msg_age(days: int) -> str:
        msg = f"Invalid operation attempted: age {days} days [REJECTED]\n"
        msg += "Security: Negative age rejected"
        return (msg)

    @staticmethod
    def error_msg_height(height: int) -> str:
        msg = f"Invalid operation attempted: height {height}cm [REJECTED]\n"
        msg += "Security: Negative height rejected"
        return (msg)


class FloweringPlant(Plant):

    def __init__(self, gardener: str, name: str, height: int = 0, age: int = 0,
                 color: str = "no") -> None:
        super().__init__(gardener, name, height, age)
        self._color: str = ""
        self.set_color(color)

    def get_color(self) -> str:
        return (self._color)

    def set_color(self, color: str) -> Self:
        self._color = color
        return (self)

    def bloom(self) -> Self:
        return (self)


class PrizeFlower(FloweringPlant):

    def __init__(self, gardener: str, name: str, height: int = 0, age: int = 0,
                 color: str = "", prize: int = 0) -> None:
        super().__init__(gardener, name, height, age, color)
        self._prize: int = 0
        self.set_prize(prize)

    def get_prize(self) -> int:
        return (self._prize)

    def set_prize(self, prize: int) -> Self:
        self._prize = prize
        return (self)


class Tree(Plant):

    def __init__(self, gardener: str, name: str, height: int = 0, age: int = 0,
                 trunk: int = 0, shade: int = 0) -> None:
        super().__init__(gardener, name, height, age)
        self._trunk: int = 0
        self._shade: int = 0
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

    def __init__(self, gardener: str, name: str, height: int = 0, age: int = 0,
                 harvest: str = "summer", nutrition: int = 0) -> None:
        super().__init__(gardener, name, height, age)
        self._harvest: str = ""
        self._nutrition: int = 0
        self.set_harvest(harvest)
        self.set_nutrition(nutrition)

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


class GardenManager:

    _gardens: list[Garden] = []

    @classmethod
    def get_gardens(cls) -> list[Garden]:
        return (cls._gardens)

    @classmethod
    def set_gardens(cls, gardens: list[Garden]) -> list[Garden]:
        cls._gardens = gardens
        return (cls._gardens)

    class GardenStats:

        _height_test: bool = True
        _nb_gardens: int = 0

        @classmethod
        def get_nb_gardens(cls) -> int:
            return (cls._nb_gardens)

        @classmethod
        def set_nb_gardens(cls, nb: int) -> None:
            cls._nb_gardens = nb

        @classmethod
        def get_height_test(cls) -> bool:
            cls._height_test = bool(sum(
                sum(plant.get_height() for plant in garden.plants)
                for garden in GardenManager.get_gardens()))
            return (cls._height_test)

    @classmethod
    def create_garden_network(cls, gardener: str) -> Garden:
        garden = next((g for g in cls.get_gardens()
                       if g.get_gardener() == gardener), None)
        if garden is None:
            garden = Garden(gardener)
            cls._gardens.append(garden)
        return (garden)

    @classmethod
    def add_plant(cls, p: dict) -> Plant:
        garden: Garden
        plant: Plant
        garden = cls.create_garden_network(p["gardener"])
        match p["type"]:
            case "flower":
                plant = FloweringPlant(garden.get_gardener(), p["name"],
                                       p["height"], p["age"],
                                       p["color"])
            case "prizeflower":
                plant = PrizeFlower(garden.get_gardener(), p["name"],
                                    p["height"], p["age"],
                                    p["color"], p["prize"])
            case "tree":
                plant = Tree(garden.get_gardener(), p["name"],
                             p["height"], p["age"],
                             p["trunk"], p["shade"])
            case "vegetable":
                plant = Vegetable(garden.get_gardener(), p["name"],
                                  p["height"], p["age"],
                                  p["harvest"], p["nutrition"])
            case _:
                plant = Plant(garden.get_gardener(), p["name"],
                              p["height"], p["age"])
        garden.plants.append(plant)
        cls.GardenStats.set_nb_gardens(cls.GardenStats.get_nb_gardens() + 1)
        return (plant)

    @classmethod
    def grow_plant(cls, grow: dict) -> Plant:
        garden: Garden
        garden = cls.create_garden_network(grow["gardener"])
        plant = next((p for p in garden.plants
                      if p.get_name() == grow["name"]), None)
        if plant is None:
            plant = cls.add_plant({"gardener": grow["gardener"],
                                   "type": "plant",
                                   "name": grow["name"],
                                   "height": 0,
                                   "age": 0})
        plant.set_height(plant.get_height() + grow["grow"])
        plant.set_grow(plant.get_grow() + grow["grow"])
        return (plant)


def ft_creat_gardens() -> None:
    streamjson = [
        {"gardener": "Alice", "type": "flower", "name": "Rose",
         "height": 25, "age": 15, "color": "red"},
        {"gardener": "Alice", "type": "prizeflower", "name": "Sunflower",
         "height": 50, "age": 12, "color": "yellow", "prize": 10},
        {"gardener": "Alice", "type": "tree", "name": "Oak Tree",
         "height": 500, "age": 1825, "trunk": 50, "shade": 78},
        {"gardener": "Tatiana", "type": "flower", "name": "Tulipe",
         "height": 42, "age": 16, "color": "blue"},
        {"gardener": "Bob", "type": "tree", "name": "Chestnut",
         "height": 650, "age": 3650, "trunk": 64, "shade": 42},
        {"gardener": "Bob", "type": "vegetable", "name": "Tomato",
         "height": 80, "age": 90, "harvest": "summer", "nutrition": 15},
        {"gardener": "Bob", "type": "vegetable", "name": "Chili pepper",
         "height": 64, "age": 42, "harvest": "fall", "nutrition": 20}]
    for stream in streamjson:
        plant = GardenManager.add_plant(stream)
        print(f"Added {plant.get_name()} to {plant.get_gardener()}'s garden")
    print("")


def ft_grow_plant() -> None:
    streamjson = [
        {"gardener": "Alice", "name": "Rose", "grow": 1},
        {"gardener": "Alice", "name": "Sunflower", "grow": 1},
        {"gardener": "Alice", "name": "Oak Tree", "grow": 1},
        {"gardener": "Tatiana", "name": "Tulipe", "grow": 12},
        {"gardener": "Bob", "name": "Tomato", "grow": 4},
        {"gardener": "Bob", "name": "Chili pepper", "grow": 6}]
    for stream in streamjson:
        GardenManager.grow_plant(stream)
    for g in GardenManager._gardens:
        print(f"{g.get_gardener()} is helping all plants grow...")
        for p in g.plants:
            print(f"{p.get_name()} grew {p.get_grow()}cm")
        print("")


def ft_garden_report() -> None:
    for g in GardenManager.get_gardens():
        print(f"=== {g.get_gardener()}'s Garden Report ===")
        print("Plants in garden:")
        for p in g.plants:
            print(f"- {p.get_name()}: {p.get_height()}cm", end="")
            if isinstance(p, FloweringPlant):
                print(f" {p.get_color()} flowers (blooming)")
            elif isinstance(p, PrizeFlower):
                print(f" {p.get_color()} flowers (blooming)", end="")
                print(f" Prize points: {p.get_prize()}")
            else:
                print("")
        print("")
        print(f"Plants added: {g.plants.__len__()},", end="")
        print(f"Total growth: {g.get_total_grow()}cm")
        print("Plant types:", end="")
        for tp, total_tp in g.get_types_plants().items():
            print(f" {total_tp} {tp}", end="")
        print("")
        print("")


def ft_global_stats() -> None:
    print("Height validation test:", end=" ")
    print(f"{GardenManager.GardenStats.get_height_test()}")
    print("Garden scores -", end="")
    for g in GardenManager._gardens:
        print(f" {g.get_gardener()}: {g.get_score()}", end=" ")
    print("")
    print("Total gardens managed:", end=" ")
    print(f"{GardenManager.GardenStats.get_nb_gardens()}")
    print("")


def ft_garden_analytics() -> None:
    print("=== Garden Management System Demo ===")
    print("")
    ft_creat_gardens()
    ft_grow_plant()
    ft_garden_report()
    ft_global_stats()


if __name__ == "__main__":
    ft_garden_analytics()
