# Data extraction using Amplitude's Export API
# https://amplitude.com/docs/apis/analytics/export

# Load libraries
import os
import requests
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


