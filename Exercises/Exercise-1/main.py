import os
import requests
import zipfile

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]

def create_download_dir():
    if not os.path.exists("downloads"):
        os.makedirs("downloads")
        print("created downloads directory")
    else:
        print("downloads directory already exists")
        
def get_filename(url):
    return url.split("/")[-1]

def download_and_extract(url):
    filename = get_filename(url)
    zip_path = os.path.join("downloads", filename)
    
    try:
        print(f"Downloading {filename}...")
        response = requests.get(url)
        response.raise_for_status()
        
        with open(zip_path, "wb") as file:
            file.write(response.content)
        print(f"Downloaded {filename}")
        
        print(f"Extracting {filename}...")
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall("downloads")
        print(f"Extracted {filename}")
        
        # Delete the zip file after extraction
        os.remove(zip_path)
        print(f"Deleted {filename} after extraction")
        
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {filename}: {e}")
    except zipfile.BadZipFile:
        print(f"Error extracting {filename}: Not a valid zip file")
        
    

def main():
    # your code here
    create_download_dir()
    
    for url in download_uris:
        download_and_extract(url)
    

if __name__ == "__main__":
    main()
