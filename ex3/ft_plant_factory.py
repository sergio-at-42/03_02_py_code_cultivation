#!/usr/bin/env python3

class Plant:

    nb_plant: int = 0

    def __init__(self, name: str = "Unknown plant",
                 height: int = 0, age: int = 0) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age
        self.growth: int = 0
        Plant.nb_plant += 1

    def get_info(self) -> None:
        print(self.name, ":  ", self.height, sep="", end="")
        print(self.age, " days old", sep="")

    def set_age(self, days: int) -> None:
        self.set_grow(int(self.height * 0.25 * days / 7))
        self.age += days

    def set_grow(self, centimeters: int) -> None:
        self.growth = centimeters
        self.height += centimeters


def ft_creat_plant(plants: list[Plant]) -> None:
    streamline: list[tuple[str, int, int]] = [("Rose", 25, 30),
                                              ("Oak", 200, 365),
                                              ("Cactus", 15, 120),
                                              ("Sunflower", 80, 45),
                                              ("Fern", 15, 120)]
    for stream in streamline:
        plants.append(Plant(stream[0], stream[1], stream[2]))


def ft_plant_factory() -> None:

    plants: list[Plant] = []
    print("=== Plant Factory Output ===")
    ft_creat_plant(plants)
    plants.append(Plant())
    plants.append(Plant("onion"))
    for plant in plants:
        print("Created: ", plant.name, sep="", end="")
        print(" (", plant.height, "cm, ", plant.age, " days)")
    print("")
    print("Total plants created: ", Plant.nb_plant)


if __name__ == "__main__":
    ft_plant_factory()
