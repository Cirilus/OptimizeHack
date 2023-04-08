import datetime

from pydantic import BaseModel


class Date(BaseModel):
    date: datetime.date


class Event(BaseModel):
    summary: str | None
    location: str | None
    description: str | None
    start: Date | None
    end: Date | None



