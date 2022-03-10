import psycopg2
from fastapi import FastAPI
from psycopg2.extras import RealDictCursor
import time
from . import models, schemas, utils
from .database import engine, get_db
from .routers import post, user, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastAPI',
                                user='postgres', password='123',
                                cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print('You are connected to the database')
        break
    except Exception as error:
        print('failed when trying to connect to the database')
        print("Error: ", error)
        time.sleep(2)

my_posts = [{"title": "title of post1", "content": "this is the first content", "id": 1},
            {"title": "Favorite Foods", "content": "I like pizza", "id": 2}]


def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": "Hello World"}
