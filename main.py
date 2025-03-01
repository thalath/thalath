import simple_unit_convertion as SUC
import Temperature_convertion as TTC
import currency_convertion as CC
def get_int_input(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid, please input integer only..!")

def main():    
    while True:
        print("====== Main Menu==========")
        print("1. Simple unit Convertion")
        print("2. Temperature Convertion")
        print("3. Currency Convertion")
        print("4. Exit the program")
        choice = get_int_input("Select the options(1->4): ")
        if choice == 1:
            print("\n")
            simple_unit_meu()
        elif choice == 2:
            print("\n")
            temperature_menu()
        elif choice == 3:
            print("\n")
            currency_menu()
        elif choice == 4:
            break
        else:
            print("wrong choice! please choose from 1 to 4 only...!")
            
def simple_unit_meu():
    """
    1. centimeter to meter(1m = 100cm)
    2. Meter to kilometer(1km = 1000m)
    3. kilometer to meter(1km = 1000m)
    """
    while True:
        print("======Simple unit covertion Menu======")
        print("1. centimeter to meter")
        print("2. Meter to kilometer")
        print("3. kilometer to meter")
        print("4. Back to Main menu")
        choice = get_int_input("select your options(1->4): ")
        if choice == 1:
            print()
            print("=====centimeter to meter=====")
            num = get_int_input("Enter value of centimeter: ")
            result = SUC.centimeter_to_meter(num)
            print(f"{num}cm = {result}m")
        elif choice == 2:
            print()
            print("=====Meters to Kilometers=====")
            num = get_int_input("Enter value of meter: ")
            result = SUC.meter_to_kolometer(num)
            print(f"{num}m = {result}km")
        elif choice == 3:
            print
            print("=====Kilometer to Meters=====")
            num = get_int_input("Enter value of kilometer: ")
            result = SUC.kilometer_to_meter(num)
            print(f"{num}km = {result}m")
        elif choice == 4:
            print("Exting the program...")
            break

def temperature_menu():
    """
    Celsius to Farenhai formula: (9/5 * Celsius) + 32
    Farenhai to Celsius formula(Farenhai - 32 ) * 5/9
    """
    while True:
        print("======Temperature Convertion Menu======")
        print("1. Celsius to Farenheit")
        print("2. Farenheit to Celsius")
        print("3. Back to Main Menu")
        choice = get_int_input("Select the options(1->3): ")
        if choice == 1:
            print()
            print("=====Celsius to Farenheit====")
            num = get_int_input("Enter value of Centimeter: ")
            result = TTC.Celsius_to_Farenhai(num)
            print(f"{num}°C = {result}°F ")
        elif choice == 2:
            print()
            print("=====Farenheit to Celsius====")
            num = get_int_input("Enter value of Centimeter: ")
            result = TTC.Farenhai_to_Celsius(num)
            print(f"{num}°C = {result}°F ")
        elif choice == 3:
            print("Exiting the Temperature Menu to Main Menu...!")
            break
            
def currency_menu():
    """
    1. USD to Khmer riels
    2. Khmer Riels to USD
    """
    while True:
        print("======Currency Convertion Menu======")
        print("1. USD to Khmer riels")
        print("2. Khmer Riels to USD")
        print("3. Back to Main Menu")
        choice = get_int_input("Select the options(1->3): ")
        if choice == 1:
            print("=====USD to Khmer Riels====")
            num = get_int_input("Enter value of USD(Sales $1 = 4050): ")
            result = CC.USD_to_Riel(num)
            print(f"{num}USD = {result}Riels ")
        elif choice == 2:
            print("=====Riels to USD====")
            num = get_int_input("Enter value of Riels(Buy in $1 = 4100): ")
            result = CC.Riel_t0_USD(num)
            print(f"{num}Riels = {result}USD ")
        elif choice == 3:
            print("Exiting the currency menu to mani menu...!")
            break
                
if __name__ =="__main__":
    main()