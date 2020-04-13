import populartimes
import time
import geopy
import googlemaps
import json
import geopy.distance
from flask import Flask, request, jsonify

app = Flask(__name__)
gmaps = googlemaps.Client(key='AIzaSyDukmKtYeKYeR2cGThAOmTi6ZyOnBW8E-0')

@app.route('/api/v1', methods=['GET', 'POST'])
def post2():
    lat = request.get_json(request.data)["lat"]
    long = request.get_json(request.data)["long"]
    coords = (lat, long)

    # rather than just calculating one distance away, will need to calculate several to get it right
    origin = geopy.Point(lat, long)
    degrees = 250
    destination = geopy.distance.distance(kilometers=5).destination(origin, degrees)

    lat2, lon2 = destination.latitude, destination.longitude

    popular = populartimes.get("AIzaSyDukmKtYeKYeR2cGThAOmTi6ZyOnBW8E-0", ["grocery_or_supermarket"], (lat, long), (lat2, lon2))

    return json.dumps(popular)



