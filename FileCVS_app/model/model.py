from pydantic import BaseModel
from fastapi import UploadFile, File


class DetailFileData(BaseModel):
    commit_name: str
    file_name: str