import urllib.request
import json



def main():

    url = "http://maps.googleapis.com/maps/api/geocode/json?address=googleplex&sensor=false"

    response = urllib.request.urlopen(url)

    data = json.loads(response.read())

    print(data)

if __name__ == '__main__':
    main()    