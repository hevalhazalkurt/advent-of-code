# Advent of Code 2019
# Day 1 : The Tyranny of the Rocket Equation

masses = open('input.txt', 'r').readlines()

# Part 1
def total_fuel(n):
    total_fuel = 0
    for mass in n:
        mass = int(mass.strip())
        fuel = mass // 3 - 2
        total_fuel += fuel
    return total_fuel


print(total_fuel(masses))



# Part 2
def fuel_req(n):
    total_fuel = 0
    for mass in n:
        mass = int(mass.strip())
        i = mass // 3 - 2
        while i > 0:
            total_fuel += i
            i = i // 3 - 2
    return total_fuel


print(fuel_req(masses))
