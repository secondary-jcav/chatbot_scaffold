from fastapi import APIRouter, Form, Request
from fastapi.templating import Jinja2Templates

from llm.model import Model

model = Model()
router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.post("/submit", status_code=201)
async def submit(request: Request, userInput: str = Form(...)):
    response = await model.send_query(userInput)
    return templates.TemplateResponse(
        "interaction.html",
        {"request": request, "query": userInput, "response": response},
    )
