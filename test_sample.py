"""
Series of Imports required; Nomination is to locate a place on the GoogleMaps and extract Lat,Long ; geodesic for dist in Miles
"""
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
geolocator = Nominatim(user_agent="specify_your_app_name_here")

def Publisher_Score(Publisher, Places_List):
    """
    Publisher on the Map with a place or can skip this line of code altogether if we have a Lat, Long already
    """
    Publisher= "Watford"
    score=0
    Publisher_location = geolocator.geocode(Publisher, timeout=300)
    print Publisher_location
    person_loc= Publisher_location.latitude,Publisher_location.longitude
    for each in Places_List:
            each = each+" United Kingdom"
            Place_location = geolocator.geocode(each)
            temp = Place_location.latitude, Place_location.longitude
            dist = (geodesic(temp, person_loc).miles)
            print ("The distance between the two pinned places is:-  " + str(dist))
            if dist>100:
                score+=0
            elif dist<=7:
                score+=1
            else:
                dist=(dist-7)/100
                score+=dist
    print "Publisher_score is:- ", score
    return score

def Person_Score(Person, Places_List):
    """
    Publisher on the Map with a place or can skip this line of code altogether if we have a Lat, Long already
    """

    score=0
    Person_location = geolocator.geocode(Person,timeout=300)
    print Person_location
    person_loc= Person_location.latitude,Person_location.longitude
    for each in Places_List:
            each = each+" United Kingdom"
            Place_location = geolocator.geocode(each)
            temp = Place_location.latitude, Place_location.longitude
            dist = (geodesic(temp, person_loc).miles)
            print ("The distance between the two pinned places is:-  " + str(dist))
            if dist<=10:
                score += 1
            elif dist> 100:
                score+=0.05
            else:
                temp = (dist//10)/10
                temp = 1 - temp
                score+=temp
    print "Person_score is:- ", score
    return score
