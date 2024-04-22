from typing import List

from pydantic import Field

from comment.schema import CommentRead
from common.schema import TimestampMixin, OrmBase


class PlantBase(OrmBase):
    name: str = Field(min_length=1, max_length=255)
    species: str = Field(min_length=1, max_length=255)
    description: str = Field(min_length=1, max_length=1023)
    image_url: str


class PlantRead(PlantBase, TimestampMixin):
    id: int


class PlantReadWithComments(PlantRead):
    comments: List[CommentRead]


class PlantPage(OrmBase):
    items: List[PlantRead]
    current_page: int
    total_pages: int
    comments: List[CommentRead] = []


class PlantCreate(PlantBase):
    pass


class PlantUpdate(PlantBase):
    pass
