# Gravity on each planet in m/s^2
gravity = {"Mercury": 3.7, "Venus": 8.87, "Earth": 9.81, "Mars": 3.711, "Jupiter": 24.79, "Saturn": 10.44, "Uranus": 8.69, "Neptune": 11.15}

def weight_on_planet(weight, planet):
    """
    Calculate weight on a given planet
    """
    return weight * gravity[planet] / gravity["Earth"]

def main():
    print("Weight Calculator for Planets\n")
    weight = float(input("Enter your weight: "))
    unit = input("Is your weight in (K) kilograms or (L) pounds? ")
    if unit.upper() == "L":
        weight = weight * 0.45359237  # convert pounds to kilograms
    print("\nSelect a planet to calculate your weight:\n")
    for i, planet in enumerate(gravity.keys()):
        print(f"{i+1}. {planet}")
    choice = int(input("\nEnter your choice (1-8): "))
    planet = list(gravity.keys())[choice-1]
    weight_on_chosen_planet = weight_on_planet(weight, planet)
    print(f"\nYour weight on {planet} is {weight_on_chosen_planet:.2f} kg.")

if __name__ == "__main__":
    main()

