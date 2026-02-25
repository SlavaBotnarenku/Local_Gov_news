from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

posts: list[dict] = [
    {
        "id" : 1,
        "author": "Slava",
        "title": "FastApi is Awesome",
        "content": "this framewor is really easy to use and super fast",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jack Doe",
        "title": "Python is great for web developmet",
        "content": "Python is a great language for web development, and fastapi make it even better",
        "date_posted": "April 21, 2025",
    }
]
@app.get("/posts", include_in_schema=False)
@app.get("/", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(request, 'home.html', {"posts": posts, "title": "Главная страница"})

@app.get("/api/posts")
def get_posts():
    return posts