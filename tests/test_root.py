from http import HTTPStatus


def test_update_user_not_found(client):
    response = client.put(
        'users/00000000-0000-0000-0000-000000000000',
        json={
            'username': 'doesnotmatter',
            'email': 'does@not.matter',
            'password': 'whatever',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_get_users(client):
    response = client.get('users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_add_user(client):
    response = client.post(
        'users/',
        json={
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password',
        },
    )

    assert response.status_code == HTTPStatus.CREATED


def test_update_user(client):
    client.post(
        'users/',
        json={
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password',
        },
    )
    users = client.get('users/').json()['users']
    user_id = next(u['id'] for u in users if u['username'] == 'testuser')

    response = client.put(
        f'users/{user_id}',
        json={
            'username': 'updateduser',
            'email': 'updated@example.com',
            'password': 'newpassword',
        },
    )

    assert response.status_code == HTTPStatus.OK
