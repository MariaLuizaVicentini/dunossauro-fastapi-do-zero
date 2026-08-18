from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from dunossauro_fastapi.database import get_session
from dunossauro_fastapi.models import User
from dunossauro_fastapi.schemas import (
    Message,
    UserList,
    UserPublic,
    UserSchema,
)
from dunossauro_fastapi.security import (
    get_current_user,
    get_password_hash,
)

router = APIRouter(prefix='/users', tags=['users'])


@router.post(
    '/',
    response_model=UserPublic,
)
def create_user(user: UserSchema, session: Session = Depends(get_session)):

    user_db = session.scalar(
        select(User).where((User.email == user.email) | (User.username == user.username))
    )

    user_db = User(
        username=user.username,
        email=user.email,
        password=get_password_hash(user.password),
    )

    try:
        session.add(user_db)
        session.commit()
        session.refresh(user_db)

        return user_db
    except IntegrityError:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT, detail='Username ou email ja existe'
        )


@router.get(
    '/',
    response_model=UserList,
)
def read_users(
    limit: int = 10,
    offset: int = 0,
    session: Session = Depends(get_session),
    current_user=Depends(get_current_user),
):
    users = session.scalars(select(User).limit(limit).offset(offset))
    return {'users': users}


@router.put(
    '/{user_id}',
    response_model=UserPublic,
)
def update_user(
    user_id: int,
    user: UserSchema,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    if current_user.id != user_id:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail='permissões insuficientes'
        )

    current_user.email = user.email
    current_user.username = user.username
    current_user.password = get_password_hash(user.password)

    try:
        session.add(current_user)
        session.commit()
        session.refresh(current_user)

        return current_user
    except IntegrityError:
        raise HTTPException(
            detail='Username ou email ja existe',
            status_code=HTTPStatus.CONFLICT,
        )


@router.delete(
    '/{user_id}',
    response_model=Message,
)
def delete_user(
    user_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    if current_user.id != user_id:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail='permissões insuficientes'
        )

    session.delete(current_user)
    session.commit()

    return {'message': 'Usuario deletado com sucesso'}
