import asyncio
import random
from hotel_management.reservations import ReservationSystem


async def process_payment(reservation_id, amount, datetime=None):
    """Simula el procesamiento de un pago."""
    print(f"Processing payment...")    
    reservation_mgmt = ReservationSystem() 
    new_reservation_list = reservation_mgmt.reservation_list
 
    for value in new_reservation_list:
        if reservation_id != value['reservation_id']:
            continue
        else:
            time = random.randint(1,10)
            await asyncio.sleep(time)
            return (f"{datetime} - Payment processed successfully! \n reservation_id: {value['reservation_id']} \n Email: {value['consumer_object'].email} \n Amount: {amount}")


    
