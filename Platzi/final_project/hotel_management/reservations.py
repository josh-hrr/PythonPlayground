from collections import defaultdict
from datetime import datetime

class Reservation:
    def __init__(self, reservation_id, price, room, consumer):
        self.reservation_id = reservation_id
        self.price = price
        self.room = room
        self.consumer = consumer

class ReservationSystem:
    reservation_list = []
    def __init__(self):
        print("ReservationSystem Class!")

    def add_reservation(self, reservation):
        """Agrega una nueva reserva al sistema."""
        self.reservation_list.append(
            {
                "reservation_id": reservation.reservation_id,
                "price": reservation.price,
                "room_object": reservation.room,
                "consumer_object": reservation.consumer
            }
        )

    def get_reservations(self):
        """Obtiene la lista de todas las reservas."""
        return self.reservation_list  

    def get_reservations_by_id(self, reservation_id):
        for value in self.reservation_list:
            if reservation_id != value['reservation_id']:
                continue
            else:
                return value

    def cancel_reservation(self, reservation_id):
        """Cancela una reserva existente por ID."""
        for value in self.reservation_list:  
            if reservation_id != value['reservation_id']:
                continue
            else:
                self.reservation_list.remove(value) 
                return "reservation_id removed! "
            

