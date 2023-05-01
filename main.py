import os
import json
import pyproj
from pyproj import CRS


def run():
    epsg_proj4 = {}

    for epsg in range(0, 103000):
        try:
            print(f"Checking for EPSG Code {epsg}...")

            # Attempt to create a CRS object from the EPSG code
            crs = CRS.from_epsg(epsg)

            # Check if the CRS has a valid PROJ4 string
            if crs and crs.to_proj4():
                epsg_proj4[epsg] = crs.to_proj4()

        except pyproj.exceptions.CRSError:
            # Continue to the next EPSG code if an error occurs
            continue

    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_filepath = os.path.join(script_dir, "epsg_proj4.json")

    with open(json_filepath, "w") as json_file:
        json.dump(epsg_proj4, json_file, indent=2)
        print(f"Created JSON file {json_filepath}.")


if __name__ == "__main__":
    run()
