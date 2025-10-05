'''
Space Week Day 2: Exoplanet Search
For the second day of Space Week, you are given a string where each character represents the luminosity reading of a star. Determine if the readings have detected an exoplanet using the transit method. The transit method is when a planet passes in front of a star, reducing its observed luminosity.

Luminosity readings only comprise of characters 0-9 and A-Z where each reading corresponds to the following numerical values:
Characters 0-9 correspond to luminosity levels 0-9.
Characters A-Z correspond to luminosity levels 10-35.

A star is considered to have an exoplanet if any single reading is less than or equal to 80% of the average of all readings. For example, if the average luminosity of a star is 10, it would be considered to have a exoplanet if any single reading is 8 or less.


'''

print('\n*** char to value test ****')
def char_to_value(ch):
    ch.upper()
    if '0' <= ch <= '9':
        return ord(ch) - ord('0')
    if 'A' <= ch <= 'Z':
        return ord(ch) - ord('A')+10
my_char_to_value = char_to_value('Z')
print(my_char_to_value)
 
#ord() = converts value into unicode
#chr() = converts unicode into value

print('\n***has_exoplanet***')
def has_exoplanet(readings):
    my_list = [char_to_value(c) for c in readings ]
    my_average = sum(my_list) / len(my_list)
    my_average_percentage_less_than_eighty = my_average * 0.80 
    is_exoplanet = False
    for value in my_list:
        if value <= my_average_percentage_less_than_eighty:
            is_exoplanet = True
    return is_exoplanet
    #alternative: return any(value <= my_average * 0.80 for value in my_list)
my_exoplanet = has_exoplanet('FREECODECAMP')
print(my_exoplanet)