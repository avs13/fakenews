from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from model import model
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/")
async def detect_fake_news(request: Request):
    body = await request.json()
    news = body["news"]
    print(news)
    prediccion = model(news)
    print(prediccion[0])
    return {"acurancy": str(prediccion[0])}