from fastapi import FastAPI, UploadFile, \
    File, Form, APIRouter, Request
from fastapi.middleware.cors import CORSMiddleware
import os
from utils import Git
from model.model import DetailFileData
from dotenv import load_dotenv
from fastapi.openapi.docs import (
    get_swagger_ui_html,
)

api = APIRouter()

load_dotenv()

git = Git()



@api.get("/commits/{file_name}")
def get_commits(file_name: str):
    return git.get_commits(file_name)


@api.get("/files")
def get_files():
    return git.get_files()


@api.post("/commit")
def get_commit(file: DetailFileData):
    return git.get_commit(file.commit_name, file.file_name)


@api.post("/new_commit")
async def new_commit(file_name: str = Form(...),
                     commit_name: str = Form(...),
                     file: UploadFile = File(...)):
    file = await file.read()
    return git.new_commit(file_name, commit_name, file)

app = FastAPI(redoc_url=None,
              openapi_url="/api/cvs/openapi.json",
              docs_url="/api/cvs/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api, prefix='/api/cvs', tags=['cvs'])
