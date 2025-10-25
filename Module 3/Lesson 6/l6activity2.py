def hotel_cost(nights):
    return 140 * nights

def _plane_ride_cost_(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    else:
        return 0
    
def rental_car_cost(days):
    if days >= 7:
        return 40 * days - 50
    elif days >= 3:
        return 40 * days - 20
    else:
        return 40 * days
    
def trip_cost(days, city, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + _plane_ride_cost_(city) + spending_money

print(f"Cost of Car Rental for 6 days: ${rental_car_cost(6)}")
print(f"Cost of Hotel for 6 nights: ${hotel_cost(6)}")
print(f"Cost of Plane Ride to Los Angeles: ${_plane_ride_cost_('Los Angeles')}")
print(f"Total Trip Cost for 6 days to Los Angeles with $600 spending money: ${trip_cost(6, 'Los Angeles', 600)}")
print(trip_cost(2, 'Tampa', 100))