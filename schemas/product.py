from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    url_image: str | None
    price: float
    discount: int


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    category: int

    class Config:
        orm_mode = True
