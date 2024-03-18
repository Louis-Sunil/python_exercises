'''S02Q02 Program to calculate milage using cars odometer readings'''

def milage():
    odometer_reading_before_ride = 1000
    odometer_reading_after_ride = 1150
    distance_travelled = odometer_reading_after_ride - odometer_reading_before_ride
    fuel_consumed = 6
    milage = distance_travelled / fuel_consumed
    print("Milage of your vehical for", distance_travelled,"KMs is", milage,"KMs per liter")

# Main starts from here
milage()
