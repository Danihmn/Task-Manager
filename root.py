import uuid
from http import HTTPStatus

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from schemas.user_schema import (
    UserColumn,
    UserPublicListSchema,
    UserPublicSchema,
    UserSchema,
)

router = APIRouter(prefix='/users', tags=['users'])

database: list[UserColumn] = []


@router.get(
    path='/',
    status_code=HTTPStatus.OK,
    response_class=JSONResponse,
    response_model=UserPublicListSchema,
)
def get_users() -> UserPublicListSchema:
    return UserPublicListSchema(
        users=[
            UserPublicSchema(
                id=user.id, username=user.username, email=user.email
            )
            for user in database
        ]
    )


@router.post(
    path='/',
    status_code=HTTPStatus.CREATED,
    response_class=JSONResponse,
    response_model=UserPublicSchema,
)
def create_user(user: UserSchema) -> UserPublicSchema:
    database.append(
        UserColumn(
            username=user.username, email=user.email, password=user.password
        )
    )
    return UserPublicSchema(username=user.username, email=user.email)


@router.put(
    path='/{user_id}',
    status_code=HTTPStatus.OK,
    response_class=JSONResponse,
    response_model=UserPublicSchema,
)
def update_user(user_id: uuid.UUID, user: UserSchema):
    existing_user = next(
        (u for u in database if u.id == user_id),
        None,
    )

    if existing_user is None or existing_user not in database:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=f'User with id {user_id} not found',
        )

    database[database.index(existing_user)] = UserColumn(
        **user.model_dump(), id=user_id
    )

    return UserPublicSchema(**existing_user.model_dump())
