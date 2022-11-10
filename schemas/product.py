from pydantic import BaseModel
from typing import Union


class ProductBase(BaseModel):
    name: str
    url_image: Union[str, None]
    price: float
    discount: int


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    category: int

    class Config:
        orm_mode = True
