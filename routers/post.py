from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.post("/submit", status_code=201)
async def submit(request: Request, userInput: str = Form(...)):
    words = userInput.split()
    rearranged = " ".join(reversed(words))
    response_html = f"<div class='query text-right mr-4 mt-2'>{userInput}</div><div class='response text-center mt-2'>{rearranged}</div>"
    return HTMLResponse(content=response_html)
