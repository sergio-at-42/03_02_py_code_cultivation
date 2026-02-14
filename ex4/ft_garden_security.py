#!/usr/bin/env python3

from typing import Self


class Plant:

    def __init__(self, name, height: int = 0, age: int = 0):
        self.name = name
        self.starting_age = age
        self.age = age
        self.starting_height = height
        self.height = height

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


def ft_creat_plant(stream: list) -> Plant:
    plant = Plant(stream[0], stream[1], stream[2])
    print("Plant created: ", plant.name)
    return (plant)


def ft_update_plant(plant: Plant, age: int, height: int) -> int:
    error_height: int = 0
    error_age: int = 0
    error_height = plant.set_height(height)
    print(f"Height updated: {plant.get_height()} cm", end=" ")
    print("[KO]" if error_height else "[OK]")
    error_age = plant.set_age(age)
    print(f"Age updated: {plant.get_age()} days", end=" ")
    print("[KO]" if error_age else "[OK]")
    if error_height:
        print(plant.error_msg_height(height))
    if error_age:
        print(plant.error_msg_age(age))
    print(f"\nCurrent plant: {plant.get_name()}", end=" ")
    print(f"({plant.get_height()}cm, {plant.get_age()} days)")
    return (error_height + error_age)


def ft_garden_security():
    plants: list[Plant] = []
    streamline: list[list] = [["Rose", 25, 30]]
    print("=== Plant Factory Output ===")
    for stream in streamline:
        plants.append(ft_creat_plant(stream))
    for plant in plants:
        if plant.get_name() == "Rose":
            ft_update_plant(plant, 30, 25)


if __name__ == "__main__":
    ft_garden_security()
