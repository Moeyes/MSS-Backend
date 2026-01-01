from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate

app = FastAPI()

limit = 1  # Global variable to hold the limit value

text_posts = {1: {"id": 1, "title": "First Post", "content": "This is the first post."},
              2: {"id": 2, "title": "Second Post", "content": "This is the second post."}}

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}


@app.get("/posts")
def get_all_posts(Limit: int = limit):
    if Limit:
        return list(text_posts.values())[:Limit]
    return text_posts

@app.get("/post/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(id)

@app.post("/posts")
def create_post(post: PostCreate):
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post