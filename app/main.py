from fastapi import FastAPI
from .routes import product
from . import models, database

app = FastAPI()
models.Base.metadata.create_all(bind=database.engine)
app.include_router(product.router)
