from fastapi import Body, FastAPI
from pydantic import create_model

from models.payload_models import Payload

DynamicModel = create_model('DynamicModel',
                            fruit='banana',
                            __base__=Payload)

app = FastAPI()

@app.post("/observer")
def observer(payload: DynamicModel = None):
    return payload

