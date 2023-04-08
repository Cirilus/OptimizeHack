from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
from .utils import Git
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




