
# Import modules

import folium
import gmplot

# Open the TXT file in which data is present
f = open("gps_data.txt", "r")

# Create a map object
Local_map = folium.Map(location=[0, 0], zoom_start=1)

# Create the array to store the all the co-ordinates into that
Latitudes_Array = []
Longitudes_Array = []


# For loop to read the and every line of the LTX file
for i in f.readlines():
    # Latitude = i.split(" ")[1][:-1]  # This for the data received from the SDR
    # Longitude = i.split(" ")[3][:-1] # This for data received from the GPS over the serial
    Latitude = i.split(" ")[2][4:]
    Longitude = i.split(" ")[3][4:]
    print("Latitude :", Latitude,  "Longitude :", Longitude)

    # Add the single co-ordinates into the Latitude & longitude & array to the pass the array into the gmap function
    Latitudes_Array.append(float(Latitude))
    Longitudes_Array.append(float(Longitude))

    # Add the mark on the given co-ordinates on the MAP
    folium.Marker([Latitude, Longitude], popup='GPS').add_to(Local_map)

# Create a map object with a center point and zoom level
gmap = gmplot.GoogleMapPlotter(Latitudes_Array[0], Longitudes_Array[0], 2)
# Add all the co-ordinates into the map
gmap.scatter(Latitudes_Array, Longitudes_Array, color="red", size=40, marker=True)

Local_map.save('Local_map.html') # Save the map as a html file
gmap.draw("Google_map.html") # Draw the map and save it as an HTML file