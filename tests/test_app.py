from http import HTTPStatus

from fastapi.testclient import TestClient

from app import app


def test_read_root():
    client = TestClient(app)  # arrange

    response = client.get('/')  # act

    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {'message': 'Hello, World!'}  # assert
