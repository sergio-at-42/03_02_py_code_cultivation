#!/usr/bin/env python3

class Plant:

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


def ft_garden_data() -> None:
    plants = list()
    plants.append(Plant("Rose", 25, 30))
    plants.append(Plant("Sunflower", 80, 45))
    plants.append(Plant("Cactus", 15, 120))
    print("=== Garden Plant Registry ===")
    for p in plants:
        print(p.name, ":  ", p.height, "cm, ", p.age, " days old", sep="")


if __name__ == "__main__":
    ft_garden_data()
