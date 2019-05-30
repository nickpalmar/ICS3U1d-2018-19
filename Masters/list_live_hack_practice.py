"""
Name: extreme_cold_alert.py
Purpose: given a number of temperatures and a wind speed
         determine the wind chill and whether or not there
         should be an extreme cold alert

Author: Fabroa.E

Created: 29/05/2019
"""


def windchill(temps, wspeed):
    """Give a list of wind chill temperatures based on
       temperature and wind speed

    :param temps: temperature in a list of temperatures
    :param wspeed: wind speed given by user
    :return: list of wind chill temperatures
    """

    wind_chill_temps = []
    for t in range(len(temps)):
        calculated_wind_chill = (13.12 + 0.6215*temps[t] -
                                 11.37*wspeed*0.16 +
                                 0.3965*temps[t]*wspeed*0.16)
        wind_chill_temps.append(round(calculated_wind_chill, 2))

    return wind_chill_temps


# Welcome user
print("******* Welcome to the Extreme Cold Alert Detector ***********")

# Get list of temperatures from user
user_input_temps = input("Enter the list of temperatures: ")

# Convert string of temperatures to a list
temp_list = list(map(int, user_input_temps.split()))

# Get wind speed from user
user_input_wspeed = int(input("Enter the wind speed: "))

# Convert list of temperatures to a list of wind chill temperatures
wind_chill_list = windchill(temp_list, user_input_wspeed)

# Check if there are two consecutive hours with a wind chill under -30
two_below_30 = False
index = 0

while not two_below_30 and index < len(wind_chill_list):
    if wind_chill_list[index] < -30 and wind_chill_list[index-1] < 30:
        two_below_30 = True
    index += 1


# Tell user the current conditions
if two_below_30:
    print("EXTREME COLD ALERT!")
else:
    print("Conditions are Normal")
