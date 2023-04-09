import json

from fastapi import FastAPI, HTTPException, Request, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from utils import Calendar
from models.models import Event
import os
from dotenv import load_dotenv
from googleapiclient.errors import HttpError


api = APIRouter()



load_dotenv()

file_path = os.getenv("FILE_PATH")
scopes = os.getenv("SCOPES")
calendar_id = os.getenv("CALENDAR_ID")
calendar = Calendar(file_path, scopes, calendar_id)





@api.get("/all")
def get_calendar_list():
    return calendar.get_calendar_list()


@api.get("/events")
def get_events():
    return calendar.get_events_list()


@api.post("/events")
def create_events(event: Event):
    print(Event)
    return calendar.add_event(event)


@api.delete("/events/{eventId}")
def create_events(eventId: str):
    try:
        response = calendar.delete_event(eventId)
    except HttpError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return response


@api.patch("/events/{eventId}")
def create_events(body: Event, eventId: str):
    body = json.loads(body.json(exclude_unset=True))
    try:
        response = calendar.patch_event(eventId, body)
    except HttpError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return response


app = FastAPI(redoc_url=None,
              openapi_url="/api/calendar/openapi.json",
              docs_url="/api/calendar/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api, prefix='/api/calendar', tags=['calendar'])