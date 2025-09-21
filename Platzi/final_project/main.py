import asyncio
from hotel_management.reservations import Reservation, ReservationSystem
from hotel_management.customers import Customer, CustomerManagement
from hotel_management.rooms import Room, RoomManagement
from hotel_management.payments import process_payment
from datetime import datetime

async def main():
    # Inicializar sistemas
    customer_mgmt = CustomerManagement()
    room_mgmt = RoomManagement()
    reservation_mgmt = ReservationSystem()

    # Crear habitaciones 
    room1 = Room(1, 1, True, True)
    room2 = Room(2, 1, True, True)
    room3 = Room(3, 2, True, False)

    # Crear clientes
    customer1 = Customer(1, "Alice", "alice@example.com")  
    customer2 = Customer(2, "Alice2", "alice2@example.com")

    # Crear Reservaciones
    reservacion1 = Reservation(1, 150, room1, customer1)
    reservacion2 = Reservation(2, 250, room2, customer2)
    
    # Agregar clientes
    customer_mgmt.add_customer(customer1) 
    customer_mgmt.add_customer(customer2)  

    # Agregar habitaciones
    room_mgmt.add_room(room1)
    room_mgmt.add_room(room2)
    room_mgmt.add_room(room3)

    # Agregar reservacion 
    reservation_mgmt.add_reservation(reservacion1)
    reservation_mgmt.add_reservation(reservacion2)

    # Verificar customer agregados
    print("\nget consumer by id:")
    get_customer_result = customer_mgmt.get_customer(2) 
    print(get_customer_result)

    # Verificar disponibilidad de habitaciones
    print("\ncheck room availability: ")
    room_list_result = room_mgmt.check_availability(3)
    print(room_list_result)

    # Verificar reservaciones agregadas
    print("\nget all reservations: ")
    reservation_list_result = reservation_mgmt.get_reservations()
    print(reservation_list_result)

    # Verificar reservaciones agregads por ID
    print("\nget_reservations_by_id: ")
    reservation_list_restul_by_id = reservation_mgmt.get_reservations_by_id(1)
    print(reservation_list_restul_by_id)

    # Cancelar reservacion
    print("\ncancel_reservation: ")
    cancel_reservation_result = reservation_mgmt.cancel_reservation(2)
    print(cancel_reservation_result)

    # Verificar reservaciones después de cancelar
    print("\nget all reservations after cancelling one: ")
    print(reservation_mgmt.get_reservations()) 

    # Procesar pago asincrónicamente
    print("\nprocess_payment: ")
    payment1 = await process_payment(1, 150, datetime.now())
    print(payment1)

    return "Main function completed."

if __name__ == "__main__":
    result = asyncio.run(main())
    print(result) 

