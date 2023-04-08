import datetime

from pydantic import BaseModel


class Date(BaseModel):
    date: datetime.date


class Event(BaseModel):
    summary: str
    location: str
    description: str
    start: Date
    end: Date


