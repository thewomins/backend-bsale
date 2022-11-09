from pydantic import BaseModel
from schemas.product import Product


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int
    products: list[Product] = []

    class Config:
        orm_mode = True


class CategoryOnly(BaseModel):
    id: int
    name: str
