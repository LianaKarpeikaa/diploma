from __future__ import annotations
from typing import List
from pydantic import BaseModel, Field


class Category(BaseModel):
    id: int
    name: str


class Tag(BaseModel):
    id: int
    name: str


class PetModel(BaseModel):
    id: int
    category: Category
    name: str
    photoUrls: List[str]
    tags: List[Tag]
    status: str


class PetResponse(PetModel):
    id: int = Field(..., example=123)
