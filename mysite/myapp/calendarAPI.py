
from __future__ import print_function

import datetime
import os.path
import pytz

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# from decouple import config
# from google.oauth2 import service_account
# import googleapiclient.discovery

# CAL_ID = config('CAL_ID')
# SCOPES = ['https://www.googleapis.com/auth/calendar']
SCOPES = ['https://www.googleapis.com/auth/calendar',
          'https://www.googleapis.com/auth/calendar.events',
          'https://www.googleapis.com/auth/calendar.readonly']
SERVICE_ACCOUNT_FILE = 'mysite/google-credentials.json'
API_VERSION = 'v3'
API_NAME = 'calendar'

calendar_id = 'c_kv77kr1s6so9u1t8farra11oq0@group.calendar.google.com'

def test_calendar():
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

    service = build('calendar', 'v3', credentials=creds)
    start_datetime = datetime.datetime.now(tz=pytz.utc)
    event = service.events().insert(calendarId='primary', body={
    'summary': 'Foo',
    'description': 'Bar',
    'start': {'dateTime': '2021-12-14T09:00:00-07:00'},
    'end': {'dateTime': '2021-12-14T17:00:00-07:00'},
    }).execute()

    return event
