''' S)2Q02 Program to calculate milage using cars odometer readings and calculate the
    number of stops for refuelling'''

def mileage():
    read_before_ride = 1000
    read_after_ride = 1560
    distance_travelled = read_after_ride - read_before_ride
    fuel_consumed = 25
    fuel_tank = 10
    milage = distance_travelled / fuel_consumed
    print("Milage of your vehical for", distance_travelled,"KMs is", milage,"KMs per liter")
    refill = distance_travelled / (milage * fuel_tank)
    print("Travellaer has to stop", refill,"times to cover the distance of", distance_travelled,"KMs")

#Main Starts from here

mileage()
