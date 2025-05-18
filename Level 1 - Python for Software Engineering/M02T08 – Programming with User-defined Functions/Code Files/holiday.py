'''This program computes the total cost of a holiday using functions to 
compute the different expenses with user-given inputs. 2025-05-15 EJS'''

# Destination data. Add more cities and their info as needed.
city_data = {"chicago": {"airfare": 179.99,
                        "hotel_fee": 148.49,
                        "car_fee": 65.74},
            "miami":    {"airfare": 147.49,
                        "hotel_fee": 129.49,
                        "car_fee": 60.25},
            "new york": {"airfare": 244.99,
                         "hotel_fee": 249.00,
                         "car_fee": 89.87},
            "seattle":  {"airfare": 211.38,
                         "hotel_fee": 225.47,
                         "car_fee": 75.72},
            "boston":   {"airfare": 189.18,
                         "hotel_fee" : 200.90,
                         "car_fee": 94.55}                         
            }


# Obtain user's city choice
print("Choose a city to travel to: Chicago, Miami, New York, Seattle, Boston")
city_flight = input("City choice: ").strip().lower()
while city_flight not in city_data.keys():
    city_flight = input(
        "Selection not recognized, please try again: ").strip().lower()

# Obtain other input from user. They do not have to stay in a hotel or rent
# a car, but they cannot enter negative values for either.
num_nights = -1
while num_nights < 0:
    num_nights = int(input("How many nights will you stay: "))

rental_days = -1
while rental_days < 0:
    rental_days = int(input("How many days will a rental car be needed: "))


def hotel_cost(num_nights=0):
    """
    Compute the total cost for the hotel.
    
    Parameters:
    num_nights (int): Default value 0
        The number of nights that a hotel will be rented.

    Returns:
    float: the total hotel cost in USD.                    
    """

    return city_data[city_flight]["hotel_fee"] * num_nights


def plane_cost(city_flight):
    """
    Compute the total airfare (round trip) cost.
    Since it's a vacaction, assume the user will return via plane too.
    
    Parameters:
    city_flight (str)
        The destination city.
        
    Returns:
    float: the total airfare (one-way ticket * 2) in USD
    """

    return city_data[city_flight]["airfare"] * 2


def car_rental(rental_days=0):
    """
    Compute the total fee for renting a car.
    
    Parameters:
    rental_days (int): Default value 0
        The number of days that the user will rent a car.
        
    Returns:
    float: the total car rental fee in USD"""

    return city_data[city_flight]["car_fee"] * rental_days


def holiday_cost(city_flight, num_nights=0, rental_days=0):
    """
    Compute the total cost of the holiday by summing the total fees for
    airfare, car rental, and hotel cost.
    
    Parameters:
    city_flight (str)
        The destination city.
    num_nights (int): default 0
        The number of nights that a hotel will be required.
    rental_days (int): default 0
        The number of days that a rental car will be required.
    
    Returns:
    float: the total cost in USD of all three expenses summed.
    """

    plane_fee = plane_cost(city_flight)
    hotel_fee = hotel_cost(num_nights)
    car_fee = car_rental(rental_days)

    # Round the final cost to two decimals places.
    return round((plane_fee + hotel_fee + car_fee), 2)


# Fix the grammar, capitalize the first letter of the destination.
city_name = city_flight[0].upper() + city_flight[1:]

# Print a formatted cost breakdown and total.
print(f"""\nHere is a breakdown of the expenses for your trip to {city_name}:
      \tThe total airfare is\t\t${plane_cost(city_flight):.2f}
      \tThe total hotel fee is\t\t${hotel_cost(num_nights):.2f}
      \tThe total car rental fee is\t${car_rental(rental_days):.2f}
The total cost of your trip is ${holiday_cost(
    city_flight, num_nights, rental_days)}.
Have a great trip!
      """)
