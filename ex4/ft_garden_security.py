#!/usr/bin/env python3

from typing import Self


class Plant:

    def __init__(self, name: str = "Unknown plant",
                 height: int = 0, age: int = 0) -> None:
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

    def get_info(self) -> None:
        print(self._name, ":  ", self._height, sep="", end="")
        print(self._age, " days old", sep="")


def ft_creat_plant(stream: tuple[str, int, int]) -> Plant:
    plant = Plant(stream[0], stream[1], stream[2])
    print("Plant created: ", plant.get_name())
    return (plant)


def ft_update_plant(plants: list[Plant],
                    name: str, age: int, height: int) -> int:
    error_height: int = 0
    error_age: int = 0
    plant: Plant
    plant = next(p for p in plants if p.get_name() == name)
    error_height = plant.set_height(height)
    print("------------------------------------------------------------------")
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


def ft_garden_security() -> None:
    plants: list[Plant] = []
    streamline: list[tuple[str, int, int]] = [("Rose", 25, 30),
                                              ("Sunflower", 12, 60),
                                              ("Tulipe", 10, 12)]
    print("=== Plant Factory Output ===")
    for stream in streamline:
        plants.append(ft_creat_plant(stream))
    print("")
    ft_update_plant(plants, "Rose", 60, 25)
    ft_update_plant(plants, "Sunflower", -14, 15)
    ft_update_plant(plants, "Tulipe", 60, -5)


if __name__ == "__main__":
    ft_garden_security()
