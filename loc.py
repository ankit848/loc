import gpsd

# Connect to the GPS daemon
gpsd.connect()

# Get the current location
packet = gpsd.get_current()
latitude = packet.lat
longitude = packet.lon

print("Latitude:", latitude)
print("Longitude:", longitude)
