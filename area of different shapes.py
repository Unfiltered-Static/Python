def main():
    print("\nMenu:")
    print("1. Square")
    print("2. Rectangle")
    print("3. Circle")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        side = float(input("Enter side length: "))
        area = side * side  # Area of square
        print(f"Area of square: {area}")

    elif choice == '2':
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        area = length * width  # Area of rectangle
        print(f"Area of rectangle: {area}")

    elif choice == '3':
        radius = float(input("Enter radius: "))
        area = 3.14 * (radius * radius)  # Area of circle using 3.14 for pi
        print(f"Area of circle: {area}")

    elif choice == '4':
        print("Exiting.")

    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
