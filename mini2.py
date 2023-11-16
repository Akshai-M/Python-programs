class TollGate:
    toll_rates = {
        'lcv': {'single': 220, 'double': 330},
        'bus': {'single': 460, 'double': 690},
        'car': {'single': 150, 'double':220},
        'jeep': {'single': 150, 'double':220},
        'mav': {'single': 720, 'double': 1080},
        'truck': {'single': 880, 'double': 1315}
    }

    def __init__(self):
        self.vehicle_list = []

    def add_vehicle(self, vehicle_number, vehicle_type):
        vehicle_driver_name = input("Enter vehicle driver name:")
        self.vehicle_list.append({
            'vehicle_number': vehicle_number,
            'vehicle_type': vehicle_type,
            'driver_name': vehicle_driver_name
        })
        print(f"Vehicle {vehicle_number} added successfully")

    def calculate_toll_fee(self, vehicle_type):
            if vehicle_type in TollGate.toll_rates:
                while True:
                    trip = int(input("For single trip(1)\nFor double trip(2)\nTell us what trip you want:"))
                    if trip == 1:
                        print(f"Toll fee for single trip is {TollGate.toll_rates[vehicle_type]['single']}")
                        return
                    elif trip == 2:
                        print(f"Toll fee for double trip is {TollGate.toll_rates[vehicle_type]['double']}")
                        return
                    else:
                        print("Enter a valid trip number")
                        break
            else:
                print("Enter a valid vehicle type")
                return

    def display_vehicle_details(self, vehicle_number):
        for vehicle in self.vehicle_list:
            if vehicle['vehicle_number'] == vehicle_number:
                print(f"Vehicle number: {vehicle['vehicle_number']}\nVehicle type: {vehicle['vehicle_type']}\nVehicle driver name: {vehicle['driver_name']}\n")
                return
            print(f"No vehicle found with number {vehicle_number}")

    def display_total_revenue(self):
        total_revenue = 0
        for vehicle in self.vehicle_list:
            vehicle_type = vehicle['vehicle_type']
            total_revenue += TollGate.toll_rates[vehicle_type]['single']  # Assuming single trip revenue for simplicity
        print(f"Total Revenue: {total_revenue}")

# Create an instance of TollGate outside the loop
toll_gate = TollGate()

while True:
    print("1. Add new vehicle\n2. Toll Fee\n3. Vehicle Details\n4. Display total revenue\n5.Exit")
    choice = int(input("Enter your choice:"))

    if choice == 1:
        vehicle_number = input("Enter the vehicle number:")
        vehicle_type = input("Enter the vehicle type:").lower()
        toll_gate.add_vehicle(vehicle_number, vehicle_type)

    elif choice == 2:
        vehicle_type = input("Enter the vehicle type:").lower()
        toll_gate.calculate_toll_fee(vehicle_type)

    elif choice == 3:
        v_number = input("Enter the vehicle number:")
        toll_gate.display_vehicle_details(v_number)

    elif choice == 4:
        toll_gate.display_total_revenue()
    
    else:
        break