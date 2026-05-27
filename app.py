# app.py

from fastapi import FastAPI

from pydantic import BaseModel

from main import process_text


# =========================================
# FASTAPI APP
# =========================================

app = FastAPI(

    title="Secure AI Privacy Gateway",

    description="Enterprise Privacy Middleware",

    version="1.0.0"
)


# =========================================
# REQUEST MODEL
# =========================================

class TextRequest(BaseModel):

    text: str


# =========================================
# ROOT ENDPOINT
# =========================================

@app.get("/")

def home():

    return {

        "message": "Secure AI Privacy Gateway Running"
    }


# =========================================
# PRIVACY ENDPOINT
# =========================================

@app.post("/protect")

def protect_data(request: TextRequest):

    results = process_text(
        request.text
    )

    return results