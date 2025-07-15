# Data extraction using Amplitude's Export API
# https://amplitude.com/docs/apis/analytics/export

# Load libraries
import os
import requests       
import zipfile     
import gzip        
import shutil     
import tempfile    
from dotenv import load_dotenv
from datetime import datetime, timedelta

# Load .env file
load_dotenv()

# Read .env file
api_key = os.getenv('AMP_API_KEY')
secret_key = os.getenv('AMP_SECRET_KEY')

# Define url
url = 'https://analytics.eu.amplitude.com/api/2/export'

# Define parameters
yesterday = datetime.now()-timedelta(days=1)
start_time = yesterday.strftime('%Y%m%dT00')
end_time = yesterday.strftime('%Y%m%dT23')


# Define parameters dictionary
param= { 
    'start': start_time, 
    'end': end_time 
}

# get response 
response = requests.get(url,  params=param , auth=(api_key, secret_key))

# Make sure we only save files when the get was successful
if response.status_code == 200:
    # Save data
    data = response.content
    print('Data retrieved successfully.')
    with open('data.zip', 'wb') as file:
        file.write(data)
else:
    # Need to return error
    print(f'Error {response.status_code}: {response.text}')


# Create a temporary directory for extraction
temp_dir = tempfile.mkdtemp()

# Create local output directory
data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

# Unpack zip
with zipfile.ZipFile("data.zip", "r") as zip_ref:
    zip_ref.extractall(temp_dir)

# Locate the folders -> need file path
day_folder = next(f for f in os.listdir(temp_dir) if f.isdigit())
day_path = os.path.join(temp_dir, day_folder)

# triple unpack jsons
for root, _, files in os.walk(day_path):
    for file in files:
        if file.endswith('.gz'):
            gz_path = os.path.join(root, file)
            json_filename = file[:-3]
            output_path = os.path.join(data_dir, json_filename)
            with gzip.open(gz_path, 'rb') as gz_file, open(output_path, 'wb') as out_file:
                shutil.copyfileobj(gz_file, out_file)


