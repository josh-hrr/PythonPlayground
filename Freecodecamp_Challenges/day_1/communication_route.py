'''

Space Week Day 3: Phone Home
For day three of Space Week, you are given an array of numbers representing distances (in kilometers) between yourself, satellites, and your home planet in a communication route. Determine how long it will take a message sent through the route to reach its destination planet using the following constraints:

- The first value in the array is the distance from your location to the first satellite.
- Each subsequent value, except for the last, is the distance to the next satellite.
- The last value in the array is the distance from the previous satellite to your home planet.
- The message travels at 300,000 km/s.
- Each satellite the message passes through adds a 0.5 second transmission delay.
- Return a number rounded to 4 decimal places, with trailing zeros removed.

'''

# speed: 300,000km/s
# adds 0.5: starting at index 0 every subsequent value, excluding the last value.
def send_message(route): 
    distance_sum = sum(route)   
    transmission_delay = 0 
    route_length = 0 
    while(route_length < len(route)-1): 
        route_length += 1
        transmission_delay += 0.5  
    speed_per_second = distance_sum / 300000
    total_speed_per_second = speed_per_second + transmission_delay
    formatted_up_to_four_decimals = "{:.4f}".format(total_speed_per_second) 
    print(formatted_up_to_four_decimals)
    return float(formatted_up_to_four_decimals)

send_message([1000000, 500000000, 1000000]) # 1.6672