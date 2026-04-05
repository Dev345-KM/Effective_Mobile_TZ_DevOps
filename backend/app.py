from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()


@app.get("/", response_class=PlainTextResponse)
async def read_query():
    return 'Hello from Effective Mobile!'


@app.get("/healthcheck")
async def health_check():
    return {"status": "ok"}
