from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate, PostResponse



app = FastAPI()

text_posts = {
    1: {"title": "New post", "content": "This is my first post"},
    2: {"title": "FastAPI", "content": "FastAPI is awesome!"},
    3: {"title": "Another post", "content": "Just another post content"},
    4: {"title": "Last post", "content": "This is the last post"},
    5: {"title": "Extra post", "content": "This is an extra post"},
    6: {"title": "Sample post", "content": "This is a sample post content"},
    7: {"title": "Demo post", "content": "This is a demo post content"},
    8: {"title": "Test post", "content": "This is a test post content"},
    9: {"title": "Hello World", "content": "Hello World content"},
    10: {"title": "Final post", "content": "This is the final post content"}
}

@app.get("/posts")
def get_all_posts(limit: int | None = None ):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts


@app.get("/posts/{id}")
def get_post(id: int) -> PostResponse:
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(id)


@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
    new_id = max(text_posts.keys()) + 1
    new_post = {"title": post.title, "content": post.content}
    text_posts[new_id] = new_post
    return PostResponse(id=new_id, **new_post)

