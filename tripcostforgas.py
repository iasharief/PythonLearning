'''

This program figures out the fuel cost of any given trip. 
My inputs are the number of miles driven, price for each galllon of fuel, and the car's fuel efficiency.


'''
miles_driven = float(input('Distance to destination in miles: '))

fuel_price_per_gallon = float(input('Price of gas per gallon: $'))

fuel_efficiency = float(input('Car fuel efficiency: '))

one_way_cost = miles_driven / fuel_efficiency * fuel_price_per_gallon

rounded_one_way_cost = round(one_way_cost,2)

print ("The fuel cost for one way is: ${} ".format(rounded_one_way_cost))

round_trip_cost = rounded_one_way_cost + rounded_one_way_cost

print ("The fuel cost for a round trip is ${}".format(round_trip_cost))