from decimal import Decimal
from math import radians, sin, cos, sqrt, atan2


class DistanceMeasurement:

    def city_distance(self, city1, city2):
        '''
        description: This function calculates differnce between latitudes and longitudes of 2 cities and returns an
        output in KM with 2 decimal places. The R value denotes earth's radius in KMs
        :param city1: Coordinates of first city
        :param city2: Coordinates of second city
        :return distance: difference in distance  bewteen 2 cities in Km
        '''

        R = 6373.0

        city1_coord = city1.split(",")
        city2_coord = city2.split(",")

        city1_lat = radians(Decimal(city1_coord[0].split(" ")[0]))
        city1_long = radians(Decimal(city1_coord[1].strip().split(" ")[0]))
        city2_lat = radians(Decimal(city2_coord[0].split(" ")[0]))
        city2_long = radians(Decimal(city2_coord[1].strip().split(" ")[0]))

        difference_lat = city2_lat - city1_lat
        difference_long = city2_long - city1_long

        a = sin(difference_lat / 2) ** 2 + cos(city1_lat) * cos(city2_lat) * sin(difference_long / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        differnce_btw_cities = R * c

        return round(differnce_btw_cities, 2)


city1 = "51.5074 N, 0.1278 W"
city2 = "48.8566 N, 2.3522 E"
dm = DistanceMeasurement()
print("City 1:" + str(city1))
print("City 2:" + str(city2))
print("City 1 and City 2 are " + str(dm.city_distance(city1, city2)) + " km apart")