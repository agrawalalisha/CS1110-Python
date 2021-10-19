# Alisha Agrawal (aa3se) Matthew Beyer (mtb4xmx)
import math

filename = 'chickfila.csv'
connection = open(filename)
contents = connection.read()
locations_list = contents.split("\n")
print(locations_list)


# DO NOT MODIFY the following function; use as is
def distance_between(lat_1, lon_1, lat_2, lon_2):
    """
    Uses the "great circle distance" formula and the circumference of the earth
    to convert two GPS coordinates to the miles separating them
    :param lat_1:
    :param lon_1:
    :param lat_2:
    :param lon_2:
    :return: 
    """
    lat_1, lon_1 = math.radians(lat_1), math.radians(lon_1)
    lat_2, lon_2 = math.radians(lat_2), math.radians(lon_2)
    theta = lon_1 - lon_2
    dist = math.sin(lat_1) * math.sin(lat_2) + math.cos(lat_1) * math.cos(lat_2) * math.cos(theta)
    dist = math.acos(dist)
    dist = math.degrees(dist)
    dist = dist * 69.06  # 69.09 = circumference of earth in miles / 360 degrees
    return dist


lat = int(input("Enter a latitude: "))
long = int(input("Enter a longitude: "))

for r in range(len(locations_list)):
    locations_list = locations_list[r].split(",")
    print(locations_list)
    distance = distance_between(lat, long, locations_list[0], locations_list[1])
    # min_list = [1000000]
    # min_list[1] = distance
    # if min_list[0] > min_list[1]:
    # minimum = min_list[1]
    # else:
    # minimum = min_list[0]
