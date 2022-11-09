from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from routes.products import product
from routes.categories import category

app = FastAPI(
    title="Api [nombre app]",
    description="this is a REST API using fastapi and mongodb",
    version="0.9.0",
)

app.include_router(product)
app.include_router(category)

origins = [
    "http://127.0.0.1:5573",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
