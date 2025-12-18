import googlemaps
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

gmaps = googlemaps.Client(key=os.getenv("GOOGLE_MAPS_API_KEY"))

# Take user input
origin = input("Enter your starting location: ")
destination = input("Enter your destination: ")

# Get directions
now = datetime.now()
directions_result = gmaps.directions(
    origin=origin,
    destination=destination,
    mode="driving",
    departure_time=now
)

# Extract useful info
if directions_result:
    route = directions_result[0]
    leg = route["legs"][0]
    distance = leg["distance"]["text"]
    duration = leg["duration"]["text"]
    start_address = leg["start_address"]
    end_address = leg["end_address"]

    print("\n Route Information:")
    print(f"From: {start_address}")
    print(f"To:   {end_address}")
    print(f"Distance: {distance}")
    print(f"Estimated time: {duration}")
else:
    print("No route found! Check your locations or try again.")