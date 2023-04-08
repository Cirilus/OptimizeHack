from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from utils import Calendar
from models.models import Event
import os
from dotenv import load_dotenv


app = FastAPI(docs_url="/", redoc_url=None)

load_dotenv()

file_path = os.getenv("FILE_PATH")
scopes = os.getenv("SCOPES")
calendar_id = os.getenv("CALENDAR_ID")
calendar = Calendar(file_path, scopes, calendar_id)


app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/calendars")
def get_calendar_list():
    return calendar.get_calendar_list()


@app.get("/events")
def get_events():
    return calendar.get_events_list()


@app.post("/events")
def create_events(event: Event):
    return calendar.add_event(event)

