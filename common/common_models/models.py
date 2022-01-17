from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class Category(BaseModel):
    """
    Category - a model defined in OpenAPI

        id: The id of this Category [Optional].
        name: The name of this Category [Optional].
    """

    id: Optional[int] = None
    name: Optional[str] = None


class Order(BaseModel):
    """
    Order - a model defined in OpenAPI

        id: The id of this Order [Optional].
        pet_id: The pet_id of this Order [Optional].
        quantity: The quantity of this Order [Optional].
        ship_date: The ship_date of this Order [Optional].
        status: The status of this Order [Optional].
        complete: The complete of this Order [Optional].
    """

    id: Optional[int] = None
    pet_id: Optional[int] = None
    quantity: Optional[int] = None
    ship_date: Optional[datetime] = None
    status: Optional[str] = None
    complete: Optional[bool] = None


class Tag(BaseModel):
    """
    Tag - a model defined in OpenAPI

        id: The id of this Tag [Optional].
        name: The name of this Tag [Optional].
    """

    id: Optional[int] = None
    name: Optional[str] = None


class Pet(BaseModel):
    """
    Pet - a model defined in OpenAPI

        id: The id of this Pet [Optional].
        category: The category of this Pet [Optional].
        name: The name of this Pet.
        photo_urls: The photo_urls of this Pet.
        tags: The tags of this Pet [Optional].
        status: The status of this Pet [Optional].
    """

    id: Optional[int] = None
    category: Optional[Category] = None
    name: str
    photo_urls: List[str]
    tags: Optional[List[Tag]] = None
    status: Optional[str] = None


class User(BaseModel):
    """
    User - a model defined in OpenAPI

        id: The id of this User [Optional].
        username: The username of this User [Optional].
        first_name: The first_name of this User [Optional].
        last_name: The last_name of this User [Optional].
        email: The email of this User [Optional].
        password: The password of this User [Optional].
        phone: The phone of this User [Optional].
        user_status: The user_status of this User [Optional].
    """

    id: Optional[int] = None
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    phone: Optional[str] = None
    user_status: Optional[int] = None


Category.update_forward_refs()
Tag.update_forward_refs()
Pet.update_forward_refs()
User.update_forward_refs()
