from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from utils import Calendar
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

