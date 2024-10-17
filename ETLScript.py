import requests
import time
corrdinate = []
def get_elevation_From_API(lat,lon):
    # Defien the URL and parameter for the request
    url = "https://api.opentopodata.org/v1/srtm30m"
    params = {
        "locations": f"{lat},{lon}" # format coordinate as lan,lon
    }

    #make a get request to the API
    reponse =requests.get(url,params=params)

    if reponse.status_code == 200:
        data = reponse.json()

        # parse and return the elevation information
        if 'results' in data and data['results'][0]['elevation'] is not None:
            elevation = data['results'][0]['elevation']
            data = [lat,lon,elevation]
            return data
            #print(f"The eleveation at {lat},{lon} is {elevation} meters.")
        else:
            return [lat,lon,"no data"]
            #print("no elevetation data is found")
    else:
        print(f"Error: unable to ftech data")

latitude = 55.021196 #34.791679, 36.679128 #55.782728, 12.478437
longitude = 12.408768
count = 0
while count < 1:
    data = get_elevation_From_API(latitude+count,longitude+count)
    corrdinate.append(data)
    count = count + 0.001
    with open("corrdinate.txt","a") as file:
        for item in data:
            file.write(str(item)+ " ")
        file.write("\n")
    time.sleep(1)
#print(corrdinate)