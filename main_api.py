from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

from main import *
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["http://localhost/", "http://localhost:3000/", ""]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)


class Input(BaseModel):
    question: str
    mode: str


@app.get("/")
def read_root():
    return "Welcome to MedRho Chat"


@app.post("/medrho/chat")
def get_reponse(input: Input, q: Union[str, None] = None):
    finalconfig_dict = run_query(input.question, input.mode)
    ans = json.dumps(finalconfig_dict)
    return ans
