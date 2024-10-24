def cel_to_fah(cel):
    return (cel * 9/5)+32

def cel_to_kel(cel):
    return cel + 273.15

def fah_to_cel(fah):
    return (fah - 32) * 5/9

def fah_to_kel(fah):
    return fah_to_cel(fah)+ 273.15

def kel_to_cel(kel):
    return kel - 273.15

def kel_to_fah(kel):
    return (cel_to_fah(kel_to_cel(kel)))

def convert_temp(value, unit):
    if unit == 'C':
        print(f"{value}°C is:")
        print(f"{cel_to_fah(value):.2f}°F")
        print(f"{cel_to_kel(value):.2f}K")
    
    elif unit == 'F':
        print(f"{value}°F is:")
        print(f"{fah_to_cel(value):.2f}°C")
        print(f"{fah_to_cel(value):.2f}K")
    
    elif unit == 'K':
        print(f"{value}K is:")
        print(f"{kel_to_cel(value):.2f}°C")
        print(f"{kel_to_fah(value):.2f}°F")

    else:
        print("Invalid unit of measurement. Please enter 'C, 'F' or 'K'.")

def main():
    value = float(input("Enter the temperature value:"))
    unit = input("Enter the unit of the temperature (C for Celsisus, F for Fahrenheit, K for Kelvin):").strip().upper()

    convert_temp(value, unit)

if __name__ == "__main__":
    main()
