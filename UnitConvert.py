# unitconvert.py

def convert_temperature():
    print("\n[Temperature Converter]")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    choice = input("> ")

    temp = float(input("Enter temperature: "))
    if choice == "1":
        result = (temp * 9/5) + 32
        print(f"{temp}°C = {result:.2f}°F")
    elif choice == "2":
        result = (temp - 32) * 5/9
        print(f"{temp}°F = {result:.2f}°C")
    elif choice == "3":
        result = temp + 273.15
        print(f"{temp}°C = {result:.2f}K")
    elif choice == "4":
        result = temp - 273.15
        print(f"{temp}K = {result:.2f}°C")
    else:
        print("Invalid option.")

def convert_distance():
    print("\n[Distance Converter]")
    print("1. Miles to Kilometers")
    print("2. Kilometers to Miles")
    print("3. Meters to Feet")
    print("4. Feet to Meters")
    choice = input("> ")

    dist = float(input("Enter distance: "))
    if choice == "1":
        print(f"{dist} mi = {dist * 1.60934:.2f} km")
    elif choice == "2":
        print(f"{dist} km = {dist / 1.60934:.2f} mi")
    elif choice == "3":
        print(f"{dist} m = {dist * 3.28084:.2f} ft")
    elif choice == "4":
        print(f"{dist} ft = {dist / 3.28084:.2f} m")
    else:
        print("Invalid option.")

def convert_weight():
    print("\n[Weight Converter]")
    print("1. Pounds to Kilograms")
    print("2. Kilograms to Pounds")
    print("3. Grams to Ounces")
    print("4. Ounces to Grams")
    choice = input("> ")

    weight = float(input("Enter weight: "))
    if choice == "1":
        print(f"{weight} lb = {weight * 0.453592:.2f} kg")
    elif choice == "2":
        print(f"{weight} kg = {weight / 0.453592:.2f} lb")
    elif choice == "3":
        print(f"{weight} g = {weight * 0.035274:.2f} oz")
    elif choice == "4":
        print(f"{weight} oz = {weight / 0.035274:.2f} g")
    else:
        print("Invalid option.")

def main():
    while True:
        print("\n=== Unit Converter ===")
        print("1. Temperature")
        print("2. Distance")
        print("3. Weight")
        print("4. Exit")
        selection = input("> ")

        if selection == "1":
            convert_temperature()
        elif selection == "2":
            convert_distance()
        elif selection == "3":
            convert_weight()
        elif selection == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()
