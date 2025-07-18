""# Author: Alastair Harris
# Class: IS 204
# Program: Fuel Mileage Calculator

# Collect vehicle information
car_make = input("Enter your car's make: ")
car_model_year = input("Enter your car's model year: ")
car_model = input("Enter your car's model: ")


print(f"\nVehicle: {car_model_year} {car_make} {car_model}\n")

# Initialize variables for trip tracking
total_mileage = 0
total_trips = 0

while True:
    # Collect trip information
    miles_driven = float(input("Enter miles driven on this trip: "))
    fuel_used = float(input("Enter fuel used (gallons) for this trip: "))
    
    # Calculate mileage
    if fuel_used > 0:
        mileage = miles_driven / fuel_used
    else:
        print("Fuel used cannot be zero. Please enter a valid amount.")
        continue
    
    # Determine fuel efficiency status
    status = "Fuel Efficient" if mileage >= 25 else "Gas Guzzler"
    
    # Display mileage result
    print(f"Fuel Mileage: {mileage:.2f} miles/gallon - {status}\n")
    
    # Update total mileage and trip count
    total_mileage += mileage
    total_trips += 1
    
    # Ask if the user wants to enter another trip
    more_trips = input("Do you have another trip to enter? (yes/no): ").strip().lower()
    if more_trips != 'yes':
        break

# Calculate and display the average mileage
if total_trips > 0:
    avg_mileage = total_mileage / total_trips
    print(f"\nAverage Fuel Mileage across {total_trips} trips: {avg_mileage:.2f} miles/gallon")
else:
    print("No trips recorded.")
