# Required info collected: (6) Time Zone or Time Zone offset

from geopy.geocoders import Nominatim as nom
import soupTheLink

def getTimezone(pCity, pState):
    geolocator = nom()
    cityState = str(pCity + " " + pState)
    location = geolocator.geocode(cityState)
    print('lat/lon: ', (location.latitude, location.longitude))
    
    GOOGLE_API_KEY = "AIzaSyBsSTNbL639s13EZm_apopCbxN3-iOySPE"
    googleApiURL = "https://maps.googleapis.com/maps/api/timezone/xml?location=" + str(location.latitude) + "," + str(location.longitude) + "&timestamp=1331161200&key=" + GOOGLE_API_KEY
    soupedGoogle = soupTheLink.soupTheLink(googleApiURL)
    timezoneId = soupedGoogle.time_zone_id.get_text()
    timezoneName = soupedGoogle.time_zone_name.get_text()
    print('timezoneId: ', timezoneId)
    print('timezoneName: ', timezoneName)
    
    if len(timezoneId) == 0:
        timezoneId = 'No timezone ID found.'
        
        if len(timezoneName) == 0:
            timezoneName = 'No timezone name found.'
    
    return timezoneId, timezoneName