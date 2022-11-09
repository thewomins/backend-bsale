from fastapi import Depends, APIRouter, HTTPException, Query
from sqlalchemy.orm import Session

from sql.database import SessionLocal
from controllers import productController
from schemas.product import Product

product = APIRouter()  # se define la ruta


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@product.get("/products/{product_id}", response_model=Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = productController.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@product.get("/products", response_model=list[Product])
def read_all_products(
    ids: list[int] | None = Query(default=None), db: Session = Depends(get_db)
):
    db_products = productController.get_all_products(db, ids)
    if db_products is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_products


@product.get("/products/inrange/{minimo}-{maximo}/", response_model=list[Product])
def read_products_in_range(
    minimo: int,
    maximo: int,
    db: Session = Depends(get_db),
    ids: list[int] | None = Query(default=None),
):
    db_products = productController.get_all_products(db, ids, minimo, maximo)
    if db_products is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_products


@product.get("/search/products/{product_name}", response_model=list[Product])
def search_product(product_name: str, db: Session = Depends(get_db)):
    db_product = productController.search_product(db, product_name.split("-"))
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product
