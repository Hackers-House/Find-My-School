from googleplaces import GooglePlaces, types
import folium
import requests
import os


def GetUserGeoLocation():

    url = 'http://ipinfo.io/json '
    payload = {}
    files = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload,
                                files=files)
    data = response.json()
    list1 = data["loc"].split(sep=",")
    list1 = [float(x) for x in list1]
    return list1


def GetHospitalLocation(userlatlong):
    Codes = os.getenv("G_API")
    google_places = GooglePlaces(Codes)
    query_result = google_places.nearby_search(
            lat_lng={'lat': userlatlong[0],
                     'lng': userlatlong[1]},
            radius=2000,
            types=[types.TYPE_SCHOOL])
    if query_result.has_attributions:
        print(query_result.html_attributions)
    namelatlng = []
    for place in query_result.places:
        namelatlng.append([str(place.name),
                          float(place.geo_location['lat']),
                          float(place.geo_location['lng'])])
    return namelatlng


def main():
    Userloc = GetUserGeoLocation()
    hosname = []
    my_map2 = folium.Map(location=[Userloc[0], Userloc[1]], zoom_start=30)
    HospitalLoc = GetHospitalLocation(Userloc)
    for valu in HospitalLoc:
        hosname.append(valu.pop(0))
    folium.Marker(location=[Userloc[0], Userloc[1]],
                  popup="You", icon=folium.Icon(
                   color='red', icon_color='white',
                   icon='cloud')).add_to(my_map2)
    for loc, Hsname in zip(HospitalLoc, hosname):
        folium.Marker(location=loc, popup=Hsname).add_to(my_map2)
    my_map2.save("application/templates/Skl.html")

