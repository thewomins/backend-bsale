from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.products import product
from routes.categories import category

app = FastAPI(
    title="Api Bsale",
    description="this is a REST API",
    version="1.0.0",
)

app.include_router(product)
app.include_router(category)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}
