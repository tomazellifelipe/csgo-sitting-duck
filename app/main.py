from fastapi import Body, FastAPI

from models.payload_models import Payload


app = FastAPI()

@app.post("/observer")
def observer(payload: Payload = None):
    return payload

