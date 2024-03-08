import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes then delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]


# Function grabs the next 100 events in a Google Calendar
def getCalendarEvents():
  creds = None

  # The file token.json will be used to grab the users access and refresh token
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)

  # If there are no credentials then allow the user to log in and store the credentials
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "ex.json", SCOPES
      )
      creds = flow.run_local_server(port=0)

    # Save the credentials for any future runs
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("calendar", "v3", credentials=creds)

    # Calling the Calendar API (Z indicates UTC time)
    now = datetime.datetime.utcnow().isoformat() + "Z"
    print("Getting the upcoming 100 events")
    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=now,
            maxResults=100,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )

    events = events_result.get("items", [])
    listOfEvents = []
    if not events:
      print("No upcoming events found.")
      return


    # Goes through each event and stores them in a list where the Name, DateTime, and Description are seperated with '/'
    for event in events:
      listOfEvents.append(event["summary"] + "/ " + event["start"].get("dateTime", event["start"].get("date")) + "/ " + event.get("description", "No notes available"))

    return listOfEvents

  #If an error occurs then print out the error
  except HttpError as error:
    print(f"An error occurred: {error}")
