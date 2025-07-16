from fastapi import FastAPI
from fastapi.responses import JSONResponse
import random
import json
import os

app = FastAPI()

# Load quotes from file once
with open(os.path.join(os.path.dirname(__file__), '../quotes.json'), 'r') as f:
    quotes = json.load(f)

@app.get("/")
def get_random_quote():
    quote = random.choice(quotes)
    return JSONResponse(content={"quote": quote})
