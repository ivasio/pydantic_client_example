# coding: utf-8

from typing import Dict, List  # noqa: F401

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from common_models.models.user import User


router = APIRouter()


@router.post(
    "/user",
    responses={
        200: {"description": "successful operation"},
    },
    tags=["user"],
    summary="Create user",
)
async def create_user(
    body: User = Body(None, description="Created user object"),
) -> None:
    """This can only be done by the logged in user."""
    ...


@router.post(
    "/user/createWithArray",
    responses={
        200: {"description": "successful operation"},
    },
    tags=["user"],
    summary="Creates list of users with given input array",
)
async def create_users_with_array_input(
    body: List[User] = Body(None, description="List of user object"),
) -> None:
    ...


@router.post(
    "/user/createWithList",
    responses={
        200: {"description": "successful operation"},
    },
    tags=["user"],
    summary="Creates list of users with given input array",
)
async def create_users_with_list_input(
    body: List[User] = Body(None, description="List of user object"),
) -> None:
    ...


@router.delete(
    "/user/{username}",
    responses={
        400: {"description": "Invalid username supplied"},
        404: {"description": "User not found"},
    },
    tags=["user"],
    summary="Delete user",
)
async def delete_user(
    username: str = Path(None, description="The name that needs to be deleted"),
) -> None:
    """This can only be done by the logged in user."""
    ...


@router.get(
    "/user/{username}",
    responses={
        200: {"model": User, "description": "successful operation"},
        400: {"description": "Invalid username supplied"},
        404: {"description": "User not found"},
    },
    tags=["user"],
    summary="Get user by user name",
)
async def get_user_by_name(
    username: str = Path(None, description="The name that needs to be fetched. Use user1 for testing. "),
) -> User:
    ...


@router.get(
    "/user/login",
    responses={
        200: {"model": str, "description": "successful operation"},
        400: {"description": "Invalid username/password supplied"},
    },
    tags=["user"],
    summary="Logs user into the system",
)
async def login_user(
    username: str = Query(None, description="The user name for login"),
    password: str = Query(None, description="The password for login in clear text"),
) -> str:
    ...


@router.get(
    "/user/logout",
    responses={
        200: {"description": "successful operation"},
    },
    tags=["user"],
    summary="Logs out current logged in user session",
)
async def logout_user(
) -> None:
    ...


@router.put(
    "/user/{username}",
    responses={
        400: {"description": "Invalid user supplied"},
        404: {"description": "User not found"},
    },
    tags=["user"],
    summary="Updated user",
)
async def update_user(
    username: str = Path(None, description="name that need to be updated"),
    body: User = Body(None, description="Updated user object"),
) -> None:
    """This can only be done by the logged in user."""
    ...
