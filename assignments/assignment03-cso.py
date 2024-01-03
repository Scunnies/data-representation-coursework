"""
In this assignment I was asked to write a program that retrieves the dataset for the 
"exchequer account (historical series)" from the CSO, and stores it into a file called "cso.json"
Student: Eleanor Sammon
"""


import requests
import json

def retrieve_cso_data():
    # link to landing page came from website https://data.gov.ie/dataset/fiq02-exchequer-account-historical-series
    url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en" 

    try:
        # GET request to the URL
        response = requests.get(url)

        # if the request was successful it will return a status code 200
        if response.status_code == 200:
            # parse the JSON data from the response
            data = response.json()

            # save  data to a JSON file
            with open("cso.json", "w") as json_file:
                json.dump(data, json_file, indent=4) #indentation for readability
            print("Data was successfully retrieved and saved to cso.json")

        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            
    # exception handling
    except Exception as e: 
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    retrieve_cso_data()
