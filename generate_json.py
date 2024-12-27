"""
    This python script auto generates a json of jpeg file names from the photos in the photos directory
    Run the script after updating the photos to ensure that the list is up to date
"""

import os
import json

def generate_json():
    """
    Scans a directory for .jpeg files and generates a JSON file listing the file names.
    """
    try:
        # List all files in the directory
        files = [file for file in os.listdir("./photos") if file.endswith('.jpeg')]
        
        # Save the file list to a JSON file
        with open("./gallery.json", 'w') as json_file:
            json.dump(files, json_file, indent=4)
        
        print(f"JSON file ./gallery.json has been created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Generate the JSON file
generate_json()
