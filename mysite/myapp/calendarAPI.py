
from __future__ import print_function

import datetime
import os.path
import pytz

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar',
          'https://www.googleapis.com/auth/calendar.events',
          'https://www.googleapis.com/auth/calendar.readonly']

# this is the json recovered from the oauth authorized credentials in cloud.developer
SERVICE_ACCOUNT_FILE = 'mysite/google-credentials.json'
API_VERSION = 'v3'
API_NAME = 'calendar'

# change to direct an specific calendar instead of a newly created
calendar_id = 'c_kv77kr1s6so9u1t8farra11oq0@group.calendar.google.com'

def test_calendar():
    # verify user an ask for authorization from the google client
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'mysite/google-credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
           
    # build the google calendar service, change first parameter to use another api from google
    service = build('calendar', 'v3', credentials=creds)
    start_datetime = datetime.datetime.now(tz=pytz.utc)

    # create an new event after being authorized
    # change 'primary' for a valid calendar_id when directed to an specific calendar

    event = service.events().insert(calendarId='primary', body={
    'summary': 'Foo',
    'description': 'Bar',
    'start': {'dateTime': '2021-12-14T09:00:00-07:00'},
    'end': {'dateTime': '2021-12-14T17:00:00-07:00'},
    }).execute()
    
    return event
