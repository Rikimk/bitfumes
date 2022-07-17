from fastapi import FastAPI
import models
from database import engine
from routers import blog, user


app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)

models.Base.metadata.create_all(engine)
