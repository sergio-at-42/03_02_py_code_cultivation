#!/usr/bin/env python3

class Plant:

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        self.growth = 0

    def get_info(self):
        print(self.name, ":  ", end="")
        print(self.height, "cm, ", end="")
        print(self.age, " days old", sep="")

    def set_age(self, days):
        self.set_grow(int(self.height * 0.25 * days / 7))
        self.age += days

    def set_grow(self, centimeters):
        self.growth = centimeters
        self.height += centimeters


def ft_disp_day(day, plants):
    print("=== Day", day, "===")
    for plant in plants:
        plant.set_age(day - 1)
        plant.get_info()
        if plant.growth != 0:
            print("Growth this week: +", plant.growth, "cm", sep="")


def ft_plant_growth():
    plants = list()
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
