#!/usr/bin/env python3

class Plant:

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        self.growth = 0

    def get_info(self):
        print(self.name, ":  ", self.height, sep="", end="")
        print(self.age, " days old", sep="")

    def set_age(self, days):
        self.set_grow(int(self.height * 0.25 * days / 7))
        self.age += days

    def set_grow(self, centimeters):
        self.growth = centimeters
        self.height += centimeters


def ft_creat_plant(stream) -> Plant:
    plant = Plant(stream[0], stream[1], stream[2])
    print("Created: ", plant.name, sep="", end="")
    print(" (", plant.height, "cm, ", plant.age, " days)")
    return (plant)


def ft_plant_factory():
    streamline = [["Rose", 25, 30],
                  ["Oak", 200, 365],
                  ["Cactus", 15, 120],
                  ["Sunflower", 80, 45],
                  ["Fern", 15, 120]]
    plants = list()
    nb_plant = 0
    print("=== Plant Factory Output ===")
    for stream in streamline:
        plants.append(ft_creat_plant(stream))
        nb_plant += 1

    print("")
    print("Total plants created: ", nb_plant)


if __name__ == "__main__":
    ft_plant_factory()
