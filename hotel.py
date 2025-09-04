import json

class HotelManagementSystem:
    def __init__(self):
        self.rooms = {}  # Dictionary to store room details
        self.room_types = {
            "single": 100,
            "double": 150,
            "suite": 250
        }  # Room types with pricing per day

    def create_room(self, room_number, guest_name, stay_duration, room_type):
        if room_number in self.rooms:
            print(f"Room {room_number} is already booked!")
        elif room_type not in self.room_types:
            print(f"Invalid room type! Choose from: {', '.join(self.room_types.keys())}")
        else:
            try:
                stay_duration = int(stay_duration)  # Ensure stay duration is an integer
                self.rooms[room_number] = {
                    'Guest Name': guest_name,
                    'Stay Duration': stay_duration,
                    'Room Type': room_type
                }
                print(f"Room {room_number} booked successfully!")
            except ValueError:
                print("Stay duration must be a valid number!")

    def read_rooms(self):
        if not self.rooms:
            print("No rooms are currently booked.")
        else:
            print("\n--- Booked Rooms ---")
            for room, details in self.rooms.items():
                total_cost = self.room_types[details['Room Type']] * details['Stay Duration']
                print(f"Room {room}: Guest Name - {details['Guest Name']}, "
                      f"Room Type - {details['Room Type']}, "
                      f"Stay Duration - {details['Stay Duration']} days, "
                      f"Total Cost - ${total_cost}")

    def update_room(self, room_number, guest_name=None, stay_duration=None, room_type=None):
        if room_number not in self.rooms:
            print(f"Room {room_number} is not booked yet!")
        else:
            if guest_name:
                self.rooms[room_number]['Guest Name'] = guest_name
            if stay_duration:
                try:
                    self.rooms[room_number]['Stay Duration'] = int(stay_duration)
                except ValueError:
                    print("Stay duration must be a valid number!")
                    return
            if room_type and room_type in self.room_types:
                self.rooms[room_number]['Room Type'] = room_type
            elif room_type:
                print(f"Invalid room type! Choose from: {', '.join(self.room_types.keys())}")
            print(f"Room {room_number} details updated successfully!")

    def delete_room(self, room_number):
        if room_number in self.rooms:
            del self.rooms[room_number]
            print(f"Room {room_number} booking canceled.")
        else:
            print(f"Room {room_number} is not booked!")

    def search_rooms_by_guest(self, guest_name):
        found = False
        for room, details in self.rooms.items():
            if details['Guest Name'].lower() == guest_name.lower():
                print(f"Room {room}: {details}")
                found = True
        if not found:
            print(f"No rooms found for guest name: {guest_name}")

    def check_availability(self):
        booked_rooms = set(self.rooms.keys())
        print("\n--- Available Rooms ---")
        print("All rooms except the booked ones are available.")
        if not booked_rooms:
            print("All rooms are available!")
        else:
            print(f"Currently booked rooms: {', '.join(booked_rooms)}")

    def save_data(self, filename="hotel_data.json"):
        with open(filename, "w") as file:
            json.dump(self.rooms, file)
        print(f"Data saved to {filename}")

    def load_data(self, filename="hotel_data.json"):
        try:
            with open(filename, "r") as file:
                self.rooms = json.load(file)
            print(f"Data loaded from {filename}")
        except FileNotFoundError:
            print(f"No saved data found in {filename}")

# Menu-driven system
def main():
    system = HotelManagementSystem()
    system.load_data()  # Load data on startup
    while True:
        print("\n--- Hotel Management System ---")
        print("1. Book a Room")
        print("2. View All Booked Rooms")
        print("3. Update Room Details")
        print("4. Cancel Room Booking")
        print("5. Search Rooms by Guest Name")
        print("6. Check Available Rooms")
        print("7. Save Data")
        print("8. Exit")
        choice = input("Enter your choice (1-8): ")
        
        if choice == '1':
            room_number = input("Enter room number: ")
            guest_name = input("Enter guest name: ")
            stay_duration = input("Enter stay duration (in days): ")
            room_type = input(f"Enter room type ({', '.join(system.room_types.keys())}): ")
            system.create_room(room_number, guest_name, stay_duration, room_type)
        elif choice == '2':
            system.read_rooms()
        elif choice == '3':
            room_number = input("Enter room number to update: ")
            guest_name = input("Enter new guest name (leave blank to keep unchanged): ").strip()
            stay_duration = input("Enter new stay duration (leave blank to keep unchanged): ").strip()
            room_type = input("Enter new room type (leave blank to keep unchanged): ").strip()
            system.update_room(room_number, guest_name or None, stay_duration or None, room_type or None)
        elif choice == '4':
            room_number = input("Enter room number to cancel: ")
            system.delete_room(room_number)
        elif choice == '5':
            guest_name = input("Enter guest name to search: ")
            system.search_rooms_by_guest(guest_name)
        elif choice == '6':
            system.check_availability()
        elif choice == '7':
            system.save_data()
        elif choice == '8':
            print("Exiting system. Goodbye!")
            system.save_data()  # Save data on exit
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
