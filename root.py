from http import HTTPStatus

from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from schemas import Message

router = APIRouter(prefix='/tasks', tags=['tasks'])


@router.get(path='/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return Message(message='Hello, World!')


@router.get(
    path='/hello', status_code=HTTPStatus.OK, response_class=HTMLResponse
)
def read_hello():
    return HTMLResponse(content='<h1>Hello, World!</h1>')
