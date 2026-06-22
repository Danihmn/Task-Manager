from http import HTTPStatus

from fastapi.testclient import TestClient

from app import app


def test_read_root():
    with TestClient(app) as client:  # arrange
        response = client.get('tasks/')  # act

    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {'message': 'Hello, World!'}  # assert


def test_read_hello():
    with TestClient(app) as client:
        response = client.get('tasks/hello')

    assert response.status_code == HTTPStatus.OK
    assert response.text == '<h1>Hello, World!</h1>'
