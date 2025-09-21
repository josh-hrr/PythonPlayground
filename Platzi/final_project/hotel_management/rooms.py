class Room:
    def __init__(self, room_number, number_of_bed, balcony, available):
        self.room_number = room_number
        self.number_of_bed = number_of_bed
        self.balcony = balcony
        self.available = available

class RoomManagement:
    rooms_list = []
    def __init__(self):
        print("RoomManagement Class!")

    def add_room(self, room):
        """Agrega una nueva habitación al sistema."""
        self.rooms_list.append(room)

    def check_availability(self, room_number):
        """Verifica si una habitación está disponible."""
        for value in self.rooms_list:
            if room_number == value.room_number:
                if value.available:
                    return "Room is available!" 
                else:
                    return "Room is not available!" 
                    
