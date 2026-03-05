import random

print("Welcome to Cab Booking Service")

name = input("Enter your name: ")
pickup = input("Enter pickup location: ")
drop = input("Enter drop location: ")

distance = float(input("Enter distance in km: "))

print("\nSelect Cab Type")
print("1. Mini (₹10 per km)")
print("2. Sedan (₹15 per km)")
print("3. SUV (₹20 per km)")

choice = int(input("Enter your choice: "))

if choice == 1:
    rate = 10
    cab_type = "Mini"
elif choice == 2:
    rate = 15
    cab_type = "Sedan"
elif choice == 3:
    rate = 20
    cab_type = "SUV"
else:
    print("Invalid choice")
    exit()

fare = distance * rate

driver_id = random.randint(1000, 9999)

print("\n----- Booking Confirmed -----")
print("Customer Name:", name)
print("Cab Type:", cab_type)
print("Driver ID:", driver_id)
print("Pickup Location:", pickup)
print("Drop Location:", drop)
print("Total Fare: ₹", fare)
print("-----------------------------")
