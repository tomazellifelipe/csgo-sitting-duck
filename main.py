from fastapi import Body, FastAPI
import pprint

app = FastAPI()

@app.post("/")
def root(teste = Body(None)):
    pprint.pprint(teste)
    return teste
