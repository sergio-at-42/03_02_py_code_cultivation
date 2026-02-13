#!/usr/bin/env python3

from typing import Self


class Plant:

    def __init__(self, name, height, age):
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

    def error_age(self, days: int) -> int:
        print("Invalid operation attempted: age", days, "days [REJECTED]")
        print("Security: Negative age rejected")
        return (1)
        
    def error_height(self, height: int) -> int:
        print("")
        print("Invalid operation attempted: height ", height, "cm [REJECTED]", sep="")
        print("Security: Negative height rejected")
        return (1)

    def get_info(self):
        print(self.name, ":  ", self.height, sep="", end="")
        print(self.age, " days old", sep="")


def ft_creat_plant(stream: list[str | int]) -> Plant:
    plant = Plant(stream[0], stream[1], stream[2])
    print("Plant created: ", plant.name)
    return (plant)


def ft_update_plant(plant: Plant, age: int, height: int) -> int:
    error_height: int = 0
    error_age: int = 0
    error_height = plant.set_height(height)
    print("Height updated: ", plant.get_height(), " cm", sep="", end=" ")
    if error_height:
        print("[KO]")
    else:
        print("[OK]")
    error_age = plant.set_age(age)
    print("Age updated: ", plant.get_age(), " cm", sep="", end=" ")
    if error_age:
        print("[KO]")
    else:
        print("[OK]")
    if error_height:
        plant.error_height(height)
    if error_age:
        plant.error_age(age)
    print("")    
    print("Current plant:", plant.name, end=" ")
    print("(", plant.get_height(), "cm,", sep="", end=" ")
    print(plant.get_age(), "days)")
    return (error_height + error_age)


def ft_garden_security():
    plants: list[Plant] = []
    nb_plant: int = 0
    streamline: list[list] = [["Rose", 25, 30],
                  ["Oak", 200, 365],
                  ["Cactus", 15, 120],
                  ["Sunflower", 80, 45],
                  ["Fern", 15, 120]]
    print("=== Plant Factory Output ===")
    for stream in streamline:
        plants.append(ft_creat_plant(stream))
        nb_plant += 1

    for plant in plants:
        if plant.name == "Rose":
            ft_update_plant(plant, 30, 25)

    for plant in plants:
        if plant.name == "Rose":
            ft_update_plant(plant, -30, -25)

if __name__ == "__main__":
    ft_garden_security()
