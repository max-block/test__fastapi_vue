import os

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

from .db import DB
from .models import Data1, Data2

load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db = DB(DATABASE_URL)


class CreateData1Params(BaseModel):
    name: str
    value: int


class CreateData2Params(BaseModel):
    name: str
    tags: list[str]


@app.router.get("/api/data1")
def get_data1_list():
    return [Data1(**d) for d in db.data1.find({}).sort("created_at", -1)]


@app.router.post("/api/data1")
def create_data1(params: CreateData1Params):
    new_data = Data1(**params.dict()).to_doc()
    new_id = db.data1.insert_one(new_data).inserted_id
    return Data1(**db.data1.find_one({"_id": new_id}))


@app.router.get("/api/data2")
def get_data2_list():
    return [Data2(**d) for d in db.data2.find({}).sort("created_at", -1)]


@app.router.post("/api/data2")
def create_data2(params: CreateData2Params):
    new_data = Data2(**params.dict()).to_doc()
    new_id = db.data2.insert_one(new_data).inserted_id
    return Data2(**db.data2.find_one({"_id": new_id}))
