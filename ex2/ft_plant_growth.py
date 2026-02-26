#!/usr/bin/env python3

class Plant:

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age
        self.growth: int = 0

    def get_info(self) -> None:
        print(self.name, ":  ", end="")
        print(self.height, "cm, ", end="")
        print(self.age, " days old", sep="")

    def set_age(self, days) -> None:
        self.set_grow(int(self.height * 0.25 * days / 7))
        self.age += days

    def set_grow(self, centimeters) -> None:
        self.growth = centimeters
        self.height += centimeters


def ft_disp_day(day: int, plants: list[Plant]) -> None:
    print("=== Day", day, "===")
    for plant in plants:
        plant.set_age(day - 1)
        plant.get_info()
        if plant.growth != 0:
            print("Growth this week: +", plant.growth, "cm", sep="")


def ft_plant_growth() -> None:
    plants: list[Plant] = []
    plants.append(Plant("Rose", 25, 30))
    plants.append(Plant("Sunflower", 80, 45))
    plants.append(Plant("Cactus", 15, 120))
    day = 1
    ft_disp_day(day, plants)
    day += 6
    ft_disp_day(day, plants)
    day += 6
    ft_disp_day(day, plants)


if __name__ == "__main__":
    ft_plant_growth()
