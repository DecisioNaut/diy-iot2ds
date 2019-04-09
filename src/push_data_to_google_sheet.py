# Import many libraries
from __future__ import print_function  
from googleapiclient.discovery import build  
from httplib2 import Http
from oauth2client import file, client, tools
from oauth2client.service_account import ServiceAccountCredentials
import datetime

import bme280

# Variables to access specific Google Sheet ... See documentation on how to derive this
MY_CREDENTIALS_FILE = 'NAME OF YOUR JSON CREDENTIAL FILE.json'
MY_SPREADSHEET_ID = 'NAME OF YOUR GSHEET'
MY_TAB_NAME = 'Daten'

def datetime_string()
    """datetime_string method:
        makes a string to push time in the right format to google sheets 
    """
    now = datetime.datetime.now()
    date = str(now.day) + "." str(now.month) + "." + str(now.year)
    time = str(now.hour) + ":" + str(now.minute) + ":" str(now.second)
    return date + " " + time

def update_sheet(sheetname, temperature, pressure, humidity):  
    """update_sheet method:
       appends a row of a sheet in the spreadsheet with the 
       the latest temperature, pressure and humidity sensor data
    """
    # Authentication, authorization step
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
    creds = ServiceAccountCredentials.from_json_keyfile_name( 
            MY_CREDENTIALS_FILE, SCOPES)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API, append the next row of sensor data
    # values is the array of rows we are updating, its a single row
    values = [ [ datetime_string(), temperature, pressure, humidity ] ]
    body = { 'values': values }
    # Call the append API to perform the operation
    result = service.spreadsheets().values().append(
                spreadsheetId=MY_SPREADSHEET_ID, 
                range=sheetname + '!A1:D1',
                valueInputOption='USER_ENTERED', 
                insertDataOption='INSERT_ROWS',
                body=body
                ).execute()                     

def main():  
    """main method:
       reads the BME280 chip to read the three sensors, then
       call update_sheets method to add that sensor data to the spreadsheet
    """
    # Read the BME280 chip
    bme = bme280.Bme280()
    bme.set_mode(bme280.MODE_FORCED)
    tempC, pressure, humidity = bme.get_data()
    pressure = pressure/100.
    # Print BME280 data in terminal
    print ('Temperature: %f C' % tempC)
    print ('Pressure: %f hPa' % pressure)
    print ('Humidity: %f %%rH' % humidity)
    # Update Google Sheet
    update_sheet(MY_TAB_NAME, tempC, pressure, humidity)

if __name__ == '__main__':  
    main()
