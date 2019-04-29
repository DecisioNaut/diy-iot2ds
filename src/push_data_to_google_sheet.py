# Import many libraries
from __future__ import print_function  
from googleapiclient.discovery import build  
from httplib2 import Http
from oauth2client import file, client, tools
from oauth2client.service_account import ServiceAccountCredentials
import datetime

import bme280

# Variables to access specific Google Sheet ... See documentation on how to derive this
MY_CREDENTIALS_FILE = 'diy-iot2ds-[numbers/characters].json'
MY_SPREADSHEET_ID = '[numbers/characters]'
MY_TAB_NAME = 'Daten'

def setup_API():
    """ Authenticate and authorize Google Sheets API
        and initialize BME280 sensor
    """
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
    creds = ServiceAccountCredentials.from_json_keyfile_name( 
            MY_CREDENTIALS_FILE, SCOPES)
    service = build('sheets', 'v4', http=creds.authorize(Http()))
    # Initialize BME280 sensor
    return service

def datetime_string():
    """datetime_string method:
        makes a string to push time in the right format to google sheets 
    """
    now = datetime.datetime.now()
    date = str(now.day) + "." + str(now.month) + "." + str(now.year)
    time = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
    return date + " " + time 

def get_data_for_gsheet():
    """get_data_for_gsheet method:
        reads data from bme280 and prepares a dictionary for writing to gsheet
    """
    bme = bme280.Bme280()
    bme.set_mode(bme280.MODE_FORCED)
    temperature, pressure, humidity = bme.get_data()
    pressure = pressure/100.
    time = datetime_string()
    values = [ [ time, temperature, pressure, humidity ] ]
    body = { 'values': values }    
    return body

def write_data_to_gsheet(service, body):
    """write_data_to_gsheet method:
        writes data into defined gsheet
    """
    service.spreadsheets().values().append(
        spreadsheetId=MY_SPREADSHEET_ID, 
        range=MY_TAB_NAME + '!A1:D1',
        valueInputOption='USER_ENTERED', 
        insertDataOption='INSERT_ROWS',
        body=body
        ).execute()    

def main():  
    """main method:
       reads the BME280 chip to read the three sensors, then
       call update_sheets method to add that sensor data to the spreadsheet
    """
    service = setup_API()

    body = get_data_for_gsheet()
    write_data_to_gsheet(service, body)
    data = body['values'][0]
    print('time: ' + data[0])
    print('temp: ' + str(data[1]))
    print('prsr: ' + str(data[2]))
    print('hmdt: ' + str(data[3]))

if __name__ == '__main__':  
    main()
