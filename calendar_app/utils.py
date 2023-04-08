import json
import pprint
from google.oauth2 import service_account
from googleapiclient.discovery import build

pp = pprint.PrettyPrinter()

class Calendar:
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    FILE_PATH = "buoyant-ability-378116-dbd342c33d89.json"
    # calendar_id = "427a4fe4761cd3c3a187849f2702592357b332fa54125608dfe290525e82c1c1@group.calendar.google.com"

    def __init__(self, file_path, scopes, calendar_id):
        credentials = service_account.Credentials.from_service_account_file(
            filename=file_path, scopes=[scopes]
        )
        self.calendar_id = calendar_id
        self.service = build('calendar', 'v3', credentials=credentials)

    def get_calendar_list(self):
        return self.service.calendarList().list().execute()

    def add_calendar(self, calendar_id):
        calendar_list_entry = {
            'id': calendar_id
        }

        return self.service.calendarList().insert(
            body=calendar_list_entry).execute()

    def get_events_list(self):
        page_token = None
        events = self.service.events().list(calendarId=self.calendar_id, pageToken=page_token).execute()
        return events

    def add_event(self, event):
        ex_event = {
            "summary": "string",
            "location": "string",
            "description": "string",
            "start": {
                'date': "2023-04-09",
            },
            "end": {
                "date": "2023-04-19",
            },
        }

        event = json.loads(event.json())

        return self.service.events().insert(calendarId=self.calendar_id, body=event).execute()

