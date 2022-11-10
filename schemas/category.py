from pydantic import BaseModel
from schemas.product import Product
from typing import List


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int
    products: List[Product] = []

    class Config:
        orm_mode = True


class CategoryOnly(BaseModel):
    id: int
    name: str
