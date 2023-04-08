from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import os
from utils import Git
from model.model import DetailFileData
from dotenv import load_dotenv

app = FastAPI(docs_url="/", redoc_url=None)

load_dotenv()

git = Git()

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/commits/{file_name}")
def get_commits(file_name: str):
    return git.get_commits(file_name)


@app.get("/files")
def get_files():
    return git.get_files()


@app.post("/commit")
def get_commit(file: DetailFileData):
    return git.get_commit(file.commit_name, file.file_name)


@app.post("/new_commit")
async def new_commit(file_name: str = Form(...),
                     commit_name: str = Form(...),
                     file: UploadFile = File(...)):
    file = await file.read()
    return git.new_commit(file_name, commit_name, file)
