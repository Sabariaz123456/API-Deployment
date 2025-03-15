from fastapi import FastAPI
import random

app = FastAPI()

messages = [
    "Hello, World!",
    "Hi there, World!",
    "Greetings, World!",
    "Hey World, what's up?",
    "Hello, Universe!"
]

@app.get("/hello")
def get_hello():
    return {"message": random.choice(messages)}
