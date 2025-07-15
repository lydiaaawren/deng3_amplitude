# Extract data from the API
# https://amplitude.com/docs/apis/analytics/export

import os
import requests 

def extract_amplitude_data(start_date, end_date, api_key, secret_key, output_file='data.zip'):
    """
    This function extracts data from Amplitude's Export API for a given date range and stores it in an output file which is called data.zip by default.
    
    Args:   
        start_time (str): Start date in format 'YYYYMMDDTHH' (e.g., '20241101T00')
        end_time (str): End time in format 'YYYYMMDDTHH' (e.g., '20250101T00')
        api_key (str): Amplitude API key
        secret_key (str): Amplitude secret key
        output_file (str): File name to be output, set by default to data.zip

    Output:
        bool: True if the extraction was successful, False otherwise    
    
    """

    # Define url
    url = 'https://analytics.eu.amplitude.com/api/2/export'


    # Define parameters dictionary
    param= { 
        'start': start_date, 
        'end': end_date
    }

    try:
        # Make GET request
        response = requests.get(url,  params=param , auth=(api_key, secret_key))

        # Check response status
        if response.status_code == 200:
            # Request was successful
            data = response.content
            print('Data retrieved successfully.')

            # Save file
            with open(output_file, 'wb') as file:
                file.write(data)
            print(f'Data saved to {output_file}')
            return True
        else:
            # Need to return error
            print(f'Error {response.status_code}: {response.text}')
            return False

    except Exception as e:
        print(f'An error has occured!: {str(e)}')
        return False