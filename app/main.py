from fastapi import FastAPI, Request, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from itsdangerous import URLSafeTimedSerializer, BadSignature
from sqlalchemy.orm import Session
from pathlib import Path
import os

from database import init_db, get_db, Lesson, Term

# ── App setup ──────────────────────────────────────────────────────────────────

app = FastAPI(title="Cloud Before Code")

BASE_DIR = Path(__file__).resolve().parent
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

# ── Auth config ────────────────────────────────────────────────────────────────

SECRET_KEY = "lunchrush-secret-2026"          # change before any real deployment
SHARED_PASSWORD = "lunchrush123"              # single shared password
serializer = URLSafeTimedSerializer(SECRET_KEY)
COOKIE_NAME = "lunchrush_session"


def make_session_token():
    return serializer.dumps("authenticated")


def verify_session(request: Request):
    token = request.cookies.get(COOKIE_NAME)
    if not token:
        return False
    try:
        value = serializer.loads(token, max_age=86400)  # 24 hours
        return value == "authenticated"
    except BadSignature:
        return False


def require_auth(request: Request):
    if not verify_session(request):
        raise HTTPException(status_code=302, headers={"Location": "/login"})


# ── Startup ────────────────────────────────────────────────────────────────────

@app.on_event("startup")
def startup():
    init_db()


# ── Routes ─────────────────────────────────────────────────────────────────────

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request, error: str = ""):
    return templates.TemplateResponse("login.html", {"request": request, "error": error})


@app.post("/login")
async def login(request: Request, password: str = Form(...)):
    if password == SHARED_PASSWORD:
        response = RedirectResponse(url="/", status_code=303)
        response.set_cookie(
            key=COOKIE_NAME,
            value=make_session_token(),
            httponly=True,
            max_age=86400,
            samesite="lax",
        )
        return response
    return templates.TemplateResponse(
        "login.html",
        {"request": request, "error": "Incorrect password. Try again."},
        status_code=401,
    )


@app.get("/logout")
async def logout():
    response = RedirectResponse(url="/login", status_code=303)
    response.delete_cookie(COOKIE_NAME)
    return response


@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request, db: Session = Depends(get_db)):
    if not verify_session(request):
        return RedirectResponse(url="/login", status_code=303)
    lessons = db.query(Lesson).order_by(Lesson.number).all()
    return templates.TemplateResponse(
        "index.html", {"request": request, "lessons": lessons}
    )


@app.get("/lesson/{number}", response_class=HTMLResponse)
async def lesson_view(number: int, request: Request, db: Session = Depends(get_db)):
    if not verify_session(request):
        return RedirectResponse(url="/login", status_code=303)
    lesson = db.query(Lesson).filter(Lesson.number == number).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    essential = [t for t in lesson.terms if t.essential == 1]
    stretch   = [t for t in lesson.terms if t.essential == 0]
    all_lessons = db.query(Lesson).order_by(Lesson.number).all()
    return templates.TemplateResponse(
        "lesson.html",
        {
            "request": request,
            "lesson": lesson,
            "essential": essential,
            "stretch": stretch,
            "all_lessons": all_lessons,
        },
    )


@app.get("/lesson/{number}/flashcards", response_class=HTMLResponse)
async def flashcards(number: int, request: Request, db: Session = Depends(get_db)):
    if not verify_session(request):
        return RedirectResponse(url="/login", status_code=303)
    lesson = db.query(Lesson).filter(Lesson.number == number).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    terms = [t for t in lesson.terms if t.essential == 1]
    return templates.TemplateResponse(
        "flashcards.html",
        {"request": request, "lesson": lesson, "terms": terms},
    )
