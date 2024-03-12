'''Program to calculate milage using cars odometer readings'''

odometer_reading_before_ride = 1000
odometer_reading_after_ride = 1150
distance_travelled = odometer_reading_after_ride - odometer_reading_before_ride
fuel_consumed = 6
#Assuming fuel consumed  6lts.
#Milage = distance travelled / fuel consumed

milage = distance_travelled / fuel_consumed

print("Milage of your vehical for", distance_travelled,"KMs is", milage,"KMs per liter")
