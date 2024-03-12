''' Program to calculate milage using cars odometer readings and calculate the
    number of stops for refuelling'''

odometer_reading_before_ride = 1000
odometer_reading_after_ride = 1560
distance_travelled = odometer_reading_after_ride - odometer_reading_before_ride
fuel_consumed = 25
fuel_tank = 10
#Assuming fuel consumed  25lts.
#Milage = distance travelled / fuel consumed

milage = distance_travelled / fuel_consumed
print("Milage of your vehical for", distance_travelled,"KMs is", milage,"KMs per liter")
refill = distance_travelled / (milage * fuel_tank)
print("Travellaer has to stop", refill,"times to cover the distance of", distance_travelled,"KMs")

